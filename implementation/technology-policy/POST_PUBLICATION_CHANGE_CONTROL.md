# Technology Policy Post-Publication Change Control

## Purpose

This standard defines how changes to the final Technology Policy publication baseline shall be governed after publication.

## Scope

This applies to changes affecting:

- Enterprise Technology Policy framework
- Enterprise Architecture Standard
- Technology Governance Standard
- Technology Lifecycle Standard
- Master Document Register
- Master Requirements Register
- Master Control Register
- Regulatory Traceability Matrix
- Evidence Library
- ARB Operating Model
- Exception and Waiver Standard
- Integration and implementation mappings
- Release manifests and publication certificates

## Change Classes

| Class | Description | Approval Required | Example |
|---|---|---|---|
| Administrative | Does not alter governance intent, obligation, control, or evidence requirement | Repository steward | Typo, broken link, minor metadata cleanup |
| Metadata | Updates ownership, status, cadence, or system-of-record metadata without changing control intent | EA / Technology Risk | Owner change, cadence correction, system reference update |
| Implementation | Updates import mappings, field mappings, workflow usage, or platform sequencing without changing baseline obligations | EA + Platform Owner | ServiceNow field update, Archer object mapping update |
| Substantive | Changes policy, standard, requirement, control, evidence obligation, ARB authority, or exception rules | Governance approval body | New requirement, modified control objective, changed ARB gate |
| Regulatory | Required due to regulatory, audit, legal, or supervisory change | Governance approval body + risk/compliance review | FFIEC/OCC/NIST mapping update with new obligation |
| Emergency | Required to address urgent operational, security, regulatory, or audit issue | Expedited governance decision with retrospective review | Immediate control correction or urgent exception rule |

## Required Change Metadata

Every governed change shall include:

| Field | Required |
|---|---|
| Change ID | Yes |
| Change class | Yes |
| Requestor | Yes |
| Owner | Yes |
| Affected artifacts | Yes |
| Business / regulatory driver | Yes |
| Risk impact | Yes |
| Control impact | Yes |
| Evidence impact | Yes |
| Approval path | Yes |
| Effective date | Yes |
| Release target | Yes |

## Change Workflow

1. Submit change request.
2. Classify change.
3. Assess impacted artifacts and object IDs.
4. Determine approval path.
5. Update affected artifacts in branch or controlled change set.
6. Validate traceability impact.
7. Approve or reject.
8. Commit and tag release if applicable.
9. Update release notes and manifest.
10. Communicate effective change.

## Traceability Impact Rules

A change may not be approved if it breaks:

- requirement-to-control mapping
- control-to-evidence mapping
- requirement-to-regulatory mapping
- standard-to-requirement mapping
- policy-to-standard hierarchy
- ARB decision authority
- exception/waiver expiration or ownership
- system-of-record mapping

## Release Rules

| Release Type | Usage |
|---|---|
| Patch release | Administrative and metadata corrections |
| Minor release | Implementation updates and non-material control refinements |
| Major release | Substantive policy, standard, control, or governance model change |
| Emergency release | Urgent risk, audit, regulatory, or operational correction |

## Anti-Patterns

The Bank shall not:

- edit published baseline artifacts without a change record
- change controls without updating evidence expectations
- add standards without mapped requirements
- add requirements without mapped controls
- change implementation mappings without platform-owner review
- allow exceptions without owner, expiration, and remediation path
- use chat history as the system of record for publication changes

## Minimum Approval Expectations

| Change Class | Minimum Approval |
|---|---|
| Administrative | Repository steward |
| Metadata | EA owner and impacted owner |
| Implementation | EA owner and platform owner |
| Substantive | Governance approval body |
| Regulatory | Governance approval body and risk/compliance |
| Emergency | Expedited decision authority with retrospective governance review |

## Effective Control

The published baseline remains authoritative until a new controlled release is approved and committed.

## Bottom Line

Publication does not end governance. It starts controlled lifecycle management.
