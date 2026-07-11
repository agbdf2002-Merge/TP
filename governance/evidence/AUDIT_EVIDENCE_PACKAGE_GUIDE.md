# Audit Evidence Package Guide

## Purpose

This guide defines how Technology Policy, Enterprise Architecture, ARB, standards, requirements, controls, regulatory traceability, and exception evidence shall be assembled into an audit-ready evidence package.

The intent is simple: evidence should be available before audit asks for it. Waiting until the examiner, internal audit, or risk partner asks for proof is not a control model. It is fire drill theater.

## Scope

This guide applies to evidence associated with:

- Enterprise Technology Policy
- Enterprise Architecture Standard
- Technology Governance Standard
- Technology Lifecycle Standard
- ARB decisions
- architecture evidence packs
- exceptions and waivers
- requirements and controls
- regulatory traceability
- lifecycle risk
- operational resilience
- third-party technology reviews
- AI and emerging technology reviews
- ServiceNow EA/APM/CSDM/CMDB objects
- Archer / ServiceNow IRM controls, issues, risks, and evidence

## Evidence Principles

| Principle | Description |
|---|---|
| Evidence or it did not happen | Assertions without artifacts shall not be treated as control evidence. |
| Evidence must be tied to an object | Every evidence item must map to a requirement, control, decision, exception, or finding. |
| Evidence must have an owner | Orphaned evidence is not reliable evidence. |
| Evidence must have a system of record | Chat, email, and slide decks are not durable control systems. |
| Evidence must be current | Stale evidence shall be flagged and remediated. |
| Evidence must support repeatability | Audit proof should not require heroics from one person. |

## Evidence Package Structure

Each audit evidence package should include:

1. Evidence package cover sheet
2. Scope statement
3. Applicable policy and standard references
4. Requirement mapping
5. Control mapping
6. Regulatory traceability mapping
7. Evidence inventory
8. ARB decision records, where applicable
9. Exceptions and waivers, where applicable
10. Risk acceptance records, where applicable
11. Open findings or remediation actions
12. Management attestation
13. Evidence aging report
14. Evidence completeness score

## Minimum Evidence Metadata

Every evidence item shall include:

| Field | Requirement |
|---|---|
| Evidence ID | Required |
| Evidence Name | Required |
| Evidence Type | Required |
| Related Requirement | Required |
| Related Control | Required |
| Owner | Required |
| System of Record | Required |
| Collection Frequency | Required |
| Collection Date | Required |
| Evidence Period | Required |
| Status | Required |
| Reviewer | Required |
| Review Date | Required |
| Retention Guidance | Required |

## Evidence Types

| Evidence Type | Example |
|---|---|
| Decision Record | ARB approved ADR |
| Register Extract | Requirements register, controls register, RTM extract |
| Review Evidence | Security architecture review, resilience review, third-party review |
| Pipeline Evidence | CI/CD control gate results |
| Monitoring Evidence | observability coverage report |
| Test Evidence | recovery test results |
| Exception Record | approved exception or waiver |
| Relationship Extract | CSDM/CMDB relationship export |
| Dashboard | governance metrics dashboard |
| Release Evidence | publication package and release notes |

## Evidence Collection Workflow

```text
Requirement
  -> Control
    -> Evidence Object
      -> System of Record
        -> Owner Attestation
          -> Reviewer Validation
            -> Audit Package
```

## Roles

| Role | Responsibility |
|---|---|
| Enterprise Architecture | owns architecture evidence definition and ARB package quality |
| Technology Risk | validates control design and evidence sufficiency |
| Control Owner | provides evidence and attests to operating effectiveness |
| System Owner | maintains system-of-record data quality |
| Internal Audit | independently tests evidence and control operation |
| Risk Owner | approves residual risk and exception/waiver disposition |

## Evidence Completeness Scoring

| Score | Definition |
|---|---|
| Green | Evidence exists, is current, mapped, reviewed, and stored in the approved system of record |
| Yellow | Evidence exists but has aging, mapping, review, or metadata gaps |
| Red | Evidence is missing, stale, ownerless, or not mapped to control objective |

## Audit Package Exit Criteria

An audit evidence package is complete only when:

- all in-scope requirements have mapped controls
- all in-scope controls have mapped evidence
- all evidence has an owner
- all evidence has a system of record
- all evidence has collection and review dates
- exceptions and waivers are included
- open findings are listed
- management attestation is captured
- residual gaps are documented

## Examiner-Ready Questions

The package should be able to answer:

1. What policy requirement applies?
2. What standard implements it?
3. What control validates it?
4. What evidence proves it operated?
5. Who owns it?
6. Where is the authoritative record?
7. How often is it reviewed?
8. What exceptions exist?
9. What risks remain open?
10. What changed since the last review?

## Anti-Patterns

The following are not acceptable steady-state practices:

- evidence stored only in email
- evidence stored only in chat history
- manually rebuilt audit packages each quarter
- unmapped screenshots
- unlabeled spreadsheets
- evidence without owner attestation
- controls without operating evidence
- requirements without control mapping
- ARB approvals without decision records
- exceptions without expiration dates

## Source Artifacts

| Artifact | Location |
|---|---|
| Evidence Library Register | `governance/evidence/evidence_library_register.csv` |
| Architecture Evidence Pack Template | `governance/templates/architecture_evidence_pack_template.md` |
| Master Requirements Register | `registers/master/master_requirements_register_expanded.csv` |
| Master Control Register | `registers/master/master_control_register_expanded.csv` |
| Regulatory Traceability Matrix | `registers/traceability/regulatory_traceability_matrix.csv` |
| ARB Operating Model | `governance/arb/ARB_OPERATING_MODEL.md` |
| Exception and Waiver Standard | `governance/exceptions/EXCEPTION_AND_WAIVER_STANDARD.md` |

## Bottom Line

The evidence package is the proof layer of the Technology Policy framework. If the requirement cannot be traced to a control and the control cannot be traced to evidence, the control plane is incomplete.
