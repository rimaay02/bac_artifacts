# Manual Penetration Testing for Broken Access Control Validation

This directory documents the manual penetration testing procedure used to
validate Broken Access Control (BAC) risks identified through static analysis.
The purpose of this documentation is to enable replication of the validation
process.

Manual penetration testing was used to determine whether statically detected
BAC patterns correspond to exploitable vulnerabilities in practice.

---

## Scope and Threat Model

The validation phase follows a semi-privileged adversary model. The attacker is
assumed to be unauthenticated or to possess low-privilege access and is capable
of:

- Sending crafted HTTP requests
- Manipulating request parameters and headers
- Inspecting responses, cookies, and headers
- Accessing backend services directly when exposed

This threat model reflects common real-world attack scenarios in open-source
web applications and guided both the selection of BAC patterns and the manual
testing strategy.

---

## Tools and Environment

Manual validation was performed locally in isolated environments using:

- Docker and Docker Compose for deployment
- Postman for crafting and sending HTTP requests
- Browser developer tools for inspecting cookies, headers, and network traffic

All testing was conducted against locally deployed instances of the analyzed
repositories to avoid impacting production systems.

---

## Validation Workflow

For each repository retained after static filtering, the following validation
workflow was applied:

1. **Repository setup**  
   Clone the repository and deploy it locally using Docker, Docker Compose, or
   the setup instructions provided by the project.

2. **Static finding inspection**  
   Review Semgrep findings to identify flagged endpoints, parameters, or access
   control logic (e.g., missing middleware, user-controlled identifiers).

3. **Manual request construction**  
   Use Postman or browser developer tools to construct unauthenticated or
   low-privilege HTTP requests targeting the flagged components.

4. **Behavioral observation**  
   Observe HTTP status codes, response bodies, headers, cookies, and any
   observable backend side effects.

5. **Classification**  
   Classify each finding as:
   - **Confirmed exploitable BAC vulnerability**, if unauthorized access or
     actions are possible, or
   - **False positive**, if access control is effectively enforced at runtime.

Only findings that enabled unauthorized access or behavior were classified as
exploitable.

---

## Case Study Documentation

Concrete worked examples are provided in the `examples/` directory. Each case
study documents:

- The repository and component flagged by static analysis
- The tested endpoint(s) or parameters
- The manual validation steps performed
- Expected secure behavior versus observed behavior
- The final vulnerability classification

These examples demonstrate how the validation workflow was applied in practice
across different BAC vulnerability patterns like unprotected routes, IDOR,
token or CORS misconfiguration.

---

## Supporting Evidence

Spreadsheets and screenshots collected during validation are
included as supporting evidence. These materials capture:

- Static analysis outputs
- HTTP requests and responses observed during testing

Screenshots and spreadsheets are intended to support transparency and auditability,
but the primary replication artifact is the documented validation procedure and
case study descriptions.

---

## Replication Notes and Limitations

Replication of manual penetration testing is subject to practical constraints.
Some repositories may no longer be deployable due to missing dependencies,
outdated configurations, or changes in external services.

As a result, while the documented procedure enables replication of the validation
process, successful execution depends on repository availability and setup
conditions at the time of replication.

---

## Ethical Considerations

All testing was performed on open-source projects in local environments.
No production systems were targeted, and no data beyond what was required
to confirm exploitability was accessed or modified.
