# Case Study: pm2panel

## Repository
https://github.com/4xmen/pm2panel

## Flagged by Static Analysis
Semgrep flagged multiple unprotected routes and potential IDOR
patterns in `pm2panel.js`, as well as insecure session cookie
configuration.

## Manual Validation Steps
1. Deploy the application locally using Docker.
2. Access administrative endpoints such as `/restart`, `/start`,
   or `/delete` with a numeric process ID as a query parameter.
3. Send requests without authentication using Postman.
4. Inspect cookies using browser developer tools.