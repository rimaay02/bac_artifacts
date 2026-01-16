# Case Study: SmartMirror

## Repository
https://github.com/Shinao/SmartMirror

## Flagged by Static Analysis
Semgrep flagged unprotected routes and user-controlled file
path parameters in `motion.js` and `server.js`.

## Manual Validation Steps
1. Deploy the SmartMirror backend locally.
2. Identify routes such as `/motion/gesture` and
   `/motion/uploadPhoto/:filepath`.
3. Send unauthenticated requests using Postman.
4. Manipulate the `:filepath` parameter to access or upload
   files.
