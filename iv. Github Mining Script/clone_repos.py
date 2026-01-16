import json
import os
import subprocess

# Load repositories from JSON
with open("github_repos.json", "r", encoding="utf-8") as file:
    repos = json.load(file)

# Create a folder to store cloned repositories
os.makedirs("cloned_repos", exist_ok=True)

# Clone all repositories in the JSON list
for repo in repos:
    repo_url = repo.get("url")
    if not repo_url:
        continue

    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join("cloned_repos", repo_name)

    if os.path.exists(repo_path):
        print(f"Skipping {repo_name}, already cloned.")
        continue

    print(f"Cloning {repo_url}...")
    try:
        subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clone {repo_url}: {e}")

print("✅ Cloning completed for all repositories.")
