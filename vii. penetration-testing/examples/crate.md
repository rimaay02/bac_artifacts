# Case Study: crate

## Repository
https://github.com/atulmy/crate

## Flagged by Static Analysis
Semgrep flagged an unprotected file upload route in
`api/src/setup/upload.js` and route handling logic in
`web/src/setup/server/load-routes.js`.

## Manual Validation Steps
1. Deploy the application locally using Docker.
2. Identify the `/upload` endpoint flagged by static analysis.
3. Send a POST request to `/upload` using Postman without any
   authentication headers or session tokens.
4. Include an arbitrary file in the request body.