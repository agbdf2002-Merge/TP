# TP-v0.2 Release Notes

## Release Name

Technology Policy Control Plane Hardening Release Candidate

## Release Classification

Release Candidate / Governance Review Draft

## Purpose

`TP-v0.2` advances the Technology Policy repository from an engineering draft baseline into a hardened governance control-plane release candidate. This release focuses on traceability completeness, import sequencing, validation automation, and publication readiness.

## Release Scope

This release adds or hardens the following capabilities:

1. Expanded Regulatory Traceability Matrix
2. Platform Import Sequencing
3. Governance Register Validation Automation
4. v0.2 Publication Readiness Checklist
5. Issue #1 progress tracking

## Major Additions

### Expanded Regulatory Traceability Matrix

Added:

`registers/traceability/regulatory_traceability_matrix_expanded.csv`

Coverage includes:

- `ETP-RQ-0001` through `ETP-RQ-0032`
- `CTRL-001` through `CTRL-032`
- `EVD-001` through `EVD-032`
- regulatory and framework mapping
- system-of-record alignment
- evidence source mapping
- owner and review cadence metadata

### Platform Import Sequencing

Added:

`integrations/import-sequencing/platform_import_sequence.md`

Defines dependency-aware sequencing for:

- ServiceNow EA/APM/CSDM/CMDB/IRM
- Archer / IRM
- ADO / Jira
- post-import reconciliation
- rollback handling
- import evidence package creation

### Governance Register Validation Automation

Added:

`tools/validation/validate_governance_registers.py`

` .github/workflows/register-validation.yml`

Validation coverage includes:

- required files
- required columns
- unique IDs
- ID format checks
- requirement-to-control mapping
- control-to-evidence mapping
- RTM relationship integrity

## Governance Impact

This release improves defensibility by ensuring that the control-plane chain can be validated across:

Policy -> Standard -> Requirement -> Control -> Evidence -> Regulation -> System of Record

## Release Integrity Criteria

The following conditions are required before this release should be treated as publication-ready:

- Expanded requirements register exists.
- Expanded controls register exists.
- Expanded RTM maps all 32 requirements to controls and evidence.
- Evidence library maps all 32 control objects to evidence objects.
- Import sequencing exists for ServiceNow, Archer/IRM, and ADO/Jira.
- Validation automation exists in GitHub Actions.
- Publication checklist for v0.2 exists.
- Issue #1 is updated with hardening status.

## Known Gaps

The following gaps remain outside this release:

- Live ServiceNow import testing has not been performed.
- Live Archer/IRM import testing has not been performed.
- ADO/Jira work item imports have not been tested.
- GitHub Actions workflow execution result has not been independently reviewed in this chat.
- Word/PDF publication package is not yet generated from the v0.2 markdown baseline.

## Recommended Next Release

`TP-v0.3` should focus on:

- live import dry-run evidence
- ServiceNow object relationship reconciliation
- Archer/IRM control evidence reconciliation
- ADO/Jira execution workflow test
- publication package generation
- executive approval pack

## Release Decision

Recommended decision state: **Ready for Governance Review**.

This release is not yet final publication. It is a hardened release candidate suitable for review by Enterprise Architecture, Technology Risk, ServiceNow platform ownership, Archer/IRM ownership, and delivery tooling owners.
