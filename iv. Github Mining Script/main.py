import requests
import os
import json
import time
from datetime import datetime, timedelta

# GitHub API URL
GITHUB_API_URL = "https://api.github.com/search/repositories"
TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise EnvironmentError("GitHub Token is missing. Set it in your environment as GITHUB_TOKEN.")

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Output configuration
PER_PAGE = 100
MAX_PAGES = 10
OUTPUT_FILE = "github_repos.json"
cutoff = datetime.utcnow() - timedelta(days=365)
ACTIVITY_CUTOFF_DATE = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")


# Split keywords into groups of ≤5 OR terms due to GitHub's query limitation
keyword_groups = [
    ["authentication", "authorization", "RBAC", "access control"],
    ["token", "JWT", "CORS", "session"],
    ["user ID", "user._id", "route", "endpoint", "express", "admin panel"]
]

def build_query(keywords):
    return f"language:JavaScript stars:>=500 ({' OR '.join(keywords)})"

def fetch_repos():
    all_repos = {}

    for group in keyword_groups:
        query = build_query(group)
        print(f"Searching with query: {query}")

        for page in range(1, MAX_PAGES + 1):
            params = {
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": PER_PAGE,
                "page": page
            }

            response = requests.get(GITHUB_API_URL, headers=HEADERS, params=params)

            if response.status_code == 200:
                data = response.json()
                items = data.get("items", [])
                for repo in items:
                    full_name = repo["full_name"]
                    if full_name not in all_repos and repo["updated_at"] >= ACTIVITY_CUTOFF_DATE:
                        all_repos[full_name] = {
                            "name": full_name,
                            "url": repo["html_url"],
                            "stars": repo["stargazers_count"],
                            "last_updated": repo["updated_at"],
                            "description": repo.get("description", "No description")
                        }

                if len(items) < PER_PAGE:
                    break
            else:
                print(f"Error: {response.status_code} - {response.json()}")
                break

            time.sleep(2)  # avoid hitting rate limits

    print(f"Total unique repositories fetched: {len(all_repos)}")
    return list(all_repos.values())

def save_results(repos):
    if not repos:
        print("No repositories found. Try modifying your search criteria.")
        return

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=4)
    print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    repos = fetch_repos()
    save_results(repos)
