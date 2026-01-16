# Case Study: nginx-jwt

## Repository
https://github.com/auth0/nginx-jwt

## Flagged by Static Analysis
Semgrep flagged unprotected backend routes in
`hosts/backend/server.js` related to missing authorization
checks.

## Manual Validation Steps
1. Deploy the project locally using Docker Compose.
2. Bypass the NGINX reverse proxy by sending requests directly
   to the backend service on port 5000.
3. Send a GET request to `/secure/admin` using Postman with an
   arbitrary or invalid Authorization header.