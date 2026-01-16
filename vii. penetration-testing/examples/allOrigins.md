# Case Study: allOrigins

## Repository
https://github.com/gnuns/allOrigins

## Flagged by Static Analysis
Semgrep flagged dynamic and permissive CORS configuration in
`app.js`, including reflective `Access-Control-Allow-Origin`
headers combined with credential support.

## Manual Validation Steps
1. Deploy the proxy locally.
2. Send a GET request through the proxy using Postman.
3. Set the `Origin` header to an arbitrary domain (e.g.,
   `https://evil.com`).
4. Inspect the response headers.