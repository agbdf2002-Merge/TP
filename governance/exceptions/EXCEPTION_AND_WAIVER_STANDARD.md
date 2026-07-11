# Exception and Waiver Standard

## Purpose

This standard defines how deviations from Enterprise Technology Policy requirements, Enterprise Architecture standards, control objectives, or approved architecture patterns are requested, reviewed, approved, tracked, remediated, and retired.

## Scope

This standard applies to:

- Technology Policy requirements
- Enterprise Architecture standards
- Architecture Review Board decisions
- Security, privacy, resilience, lifecycle, and platform controls
- ServiceNow CSDM/CMDB alignment requirements
- Regulatory traceability requirements
- Third-party technology architecture requirements
- AI and emerging technology governance requirements

## Definitions

| Term | Definition |
|---|---|
| Exception | Approved deviation from a required standard, control, or architecture pattern where an alternative approach is accepted. |
| Waiver | Time-bound deferral of a requirement, control, or standard due to implementation dependency, migration, or accepted short-term constraint. |
| Compensating Control | A control that reduces risk when the required control or standard cannot be met. |
| Risk Acceptance | Formal acknowledgement by the accountable authority that residual risk will be accepted for a defined period. |
| Remediation Plan | Approved plan to return to compliance or retire the exception/waiver. |

## Policy Rules

1. Exceptions and waivers shall be documented in the exception and waiver register.
2. Exceptions and waivers shall include a related requirement, control, and standard where applicable.
3. Exceptions and waivers shall include a business and technical rationale.
4. Exceptions and waivers shall include risk rating and compensating controls.
5. Exceptions and waivers shall include an expiration date.
6. Exceptions and waivers shall not be open-ended.
7. Exceptions and waivers shall be reviewed by the Architecture Review Board or delegated authority.
8. Exceptions and waivers affecting regulated data, customer impact, resilience, cybersecurity, or third-party risk shall include risk/compliance review.
9. Expired exceptions and waivers shall be escalated.
10. Repeated exceptions shall trigger standards, platform, or remediation review.

## Required Fields

| Field | Required | Description |
|---|---|---|
| Exception ID | Yes | Unique identifier |
| Type | Yes | Exception or waiver |
| Related Requirement | Yes | Requirement impacted |
| Related Control | Yes | Control impacted |
| Related Standard | Conditional | Standard impacted |
| Description | Yes | Description of deviation |
| Risk Rating | Yes | Residual risk rating |
| Requester | Yes | Individual or group requesting deviation |
| Approver | Yes | ARB or delegated approval authority |
| System of Record | Yes | ServiceNow, Archer, or approved repository |
| Expiration Date | Yes | Time-bound end date |
| Compensating Control | Yes | Control reducing residual risk |
| Evidence Required | Yes | Evidence needed to approve and track deviation |
| Status | Yes | Draft, submitted, approved, rejected, expired, closed |

## Approval Criteria

An exception or waiver may be approved only when:

- The business need is clear.
- The risk is understood and documented.
- The deviation is time-bound.
- Compensating controls are defined.
- The remediation path is credible.
- The residual risk is accepted by the appropriate authority.
- Evidence can be retained for audit and supervisory review.

## System of Record

The exception and waiver register seed is maintained at:

```text
registers/governance/exception_waiver_register.csv
```

The operational system of record should be ServiceNow or Archer, depending on implementation ownership.

## Escalation Triggers

Escalation is required when:

- A waiver exceeds its expiration date.
- A critical or high-risk exception lacks compensating controls.
- A repeated exception indicates a broken standard or missing platform capability.
- The exception affects customer data, regulated activity, operational resilience, or cyber risk.
- Remediation milestones are missed.

## Metrics

| Metric | Purpose |
|---|---|
| Open exceptions by domain | Standards compliance visibility |
| Waivers past due | Residual risk aging |
| Exceptions by technology | Technology debt and lifecycle risk |
| Exceptions by business capability | Business-aligned risk concentration |
| Repeated exception types | Standards or platform failure patterns |
| Average waiver age | Remediation discipline |
| Exception closure rate | Governance effectiveness |
