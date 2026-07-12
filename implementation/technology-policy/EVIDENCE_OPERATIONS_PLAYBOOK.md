# Technology Policy Evidence Operations Playbook

## Purpose

This playbook defines the operating process for collecting, reviewing, attesting, aging, and packaging evidence for the Technology Policy control plane.

## Operating Principle

Evidence proves that requirements and controls operated. If evidence cannot be located, verified, and tied to a requirement and control, the control should be treated as unproven.

## Evidence Scope

Evidence applies to:

- policy governance
- standards governance
- ARB decisioning
- architecture evidence packs
- requirements ownership
- control operation
- regulatory traceability
- exceptions and waivers
- technology lifecycle governance
- resilience and recovery
- security architecture review
- API and DevSecOps governance
- third-party technology review
- AI and emerging technology review
- CMDB/CSDM alignment
- monthly governance reporting

## Evidence Lifecycle

| State | Description | Owner |
|---|---|---|
| Required | Evidence object defined in the evidence library | EA / Risk |
| Requested | Evidence requested from control owner | EA / Control Owner |
| Submitted | Evidence provided for review | Control Owner |
| Accepted | Evidence reviewed and accepted | EA / Risk |
| Rejected | Evidence incomplete or not authoritative | EA / Risk |
| Aged | Evidence exceeds review or freshness threshold | Control Owner |
| Archived | Evidence retained for audit history | System of Record Owner |

## Minimum Evidence Metadata

Every evidence item shall include:

- evidence ID
- related requirement ID
- related control ID
- evidence owner
- system of record
- collection date
- review date
- reporting period
- evidence status
- reviewer
- retention expectation
- related ARB decision, exception, or lifecycle item where applicable

## Collection Cadence

| Evidence Type | Cadence |
|---|---|
| ARB decision records | Per decision |
| Architecture evidence packs | Per ARB submission |
| Control operation evidence | Monthly or quarterly based on control |
| Exception / waiver evidence | Monthly until closure |
| Lifecycle risk evidence | Monthly for high-risk items, quarterly otherwise |
| Regulatory traceability evidence | Quarterly |
| Metrics and scorecard evidence | Monthly |
| Publication and release evidence | Per release |

## Review Process

1. Evidence owner submits evidence to the system of record.
2. EA validates architectural completeness.
3. Technology Risk validates control and audit relevance.
4. Gaps are returned to evidence owner for remediation.
5. Accepted evidence is linked to the requirement, control, and applicable standard.
6. Aging and missing evidence are reported in the monthly governance scorecard.

## Acceptance Criteria

Evidence is accepted when it is:

- attributable to an accountable owner
- linked to a valid requirement and control
- generated from an authoritative system or approved process
- dated and reviewable
- relevant to the operating period
- complete enough for independent review
- retained in the approved system of record

## Rejection Criteria

Evidence shall be rejected when it is:

- a screenshot without context or owner
- not tied to a requirement/control
- stale beyond defined cadence
- stored only in email or chat
- missing reviewer or approval information
- contradictory to source-system data
- incomplete for audit testing

## Monthly Evidence Review Agenda

1. Missing evidence summary
2. Aging evidence summary
3. Rejected evidence items
4. High-risk controls lacking proof
5. Exception and waiver evidence status
6. Lifecycle risk evidence status
7. Upcoming audit or regulatory requests
8. Actions and accountable owners

## Evidence Metrics

| Metric | Purpose |
|---|---|
| Evidence completeness rate | Measures percent of controls with current evidence |
| Evidence aging rate | Measures stale evidence exposure |
| Rejected evidence count | Measures evidence quality problems |
| Unproven control count | Measures audit exposure |
| Exception evidence completeness | Measures waiver/exception governance quality |

## Systems of Record

| Evidence Area | Preferred System |
|---|---|
| Architecture evidence | ServiceNow EA/APM or approved repository |
| Control evidence | Archer / ServiceNow IRM |
| ARB decision records | GitHub and/or ServiceNow EA |
| Exceptions and waivers | Archer / ServiceNow IRM |
| Delivery evidence | ADO / Jira |
| Publication evidence | GitHub / document-management workflow |

## Anti-Patterns

- Treating evidence as an after-the-fact audit scramble.
- Accepting screenshots without metadata.
- Allowing evidence to live only in email.
- Not tying evidence to stable requirement/control IDs.
- Closing controls without evidence review.
- Allowing stale evidence to age silently.

## Status

Initial evidence operations playbook established for post-publication control adoption.
