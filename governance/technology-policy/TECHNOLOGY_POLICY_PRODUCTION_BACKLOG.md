# Technology Policy Production Backlog

## Purpose

This backlog identifies the remaining production work required to mature the Technology Policy repository from bootstrap to publication-ready governance infrastructure.

## Backlog Status Definitions

| Status | Definition |
|---|---|
| Not Started | Work has not begun |
| Draft | Artifact exists but requires expansion or review |
| Ready for Review | Artifact is complete enough for governance review |
| Approved | Artifact is approved for release |
| Published | Artifact is included in a controlled release package |

## Production Backlog

| Backlog ID | Work Package | Output | Owner | Priority | Status |
|---|---|---|---|---|---|
| TP-BL-001 | Requirements Register Expansion | Expand Master Requirements Register from seed to full policy requirement set | Enterprise Architecture | Critical | Not Started |
| TP-BL-002 | Control Register Expansion | Expand Master Control Register to cover all Technology Policy and standards requirements | Enterprise Architecture / Technology Risk | Critical | Not Started |
| TP-BL-003 | Regulatory Traceability Expansion | Expand RTM coverage across FFIEC, OCC, Federal Reserve, FDIC, NIST, CIS, COBIT, ISO, GLBA, SEC Reg S-P, NYDFS, TOGAF, BIAN, and CSDM | Enterprise Architecture / Compliance | Critical | Draft |
| TP-BL-004 | ServiceNow Object Mapping | Define ServiceNow EA/APM/CSDM/CMDB object mapping for policy, standards, requirements, controls, services, applications, and evidence | Enterprise Architecture / Platform Owner | High | Not Started |
| TP-BL-005 | Archer / IRM Object Mapping | Define Archer or ServiceNow IRM mapping for risks, controls, findings, issues, exceptions, and evidence | Technology Risk | High | Not Started |
| TP-BL-006 | ARB Intake Package | Create ARB intake form, submission checklist, and decision logic | Enterprise Architecture | High | Draft |
| TP-BL-007 | Exception Workflow | Create exception lifecycle workflow and escalation model | Enterprise Architecture / Technology Risk | High | Draft |
| TP-BL-008 | Technology Lifecycle Taxonomy | Expand lifecycle states, disposition values, and rationalization outcomes | Enterprise Architecture | High | Draft |
| TP-BL-009 | Architecture Principles Register | Convert principles to canonical object register | Enterprise Architecture | Medium | Not Started |
| TP-BL-010 | Architecture Pattern Catalog | Create reusable patterns for cloud, API, data, security, resilience, integration, and platform architecture | Enterprise Architecture | Medium | Not Started |
| TP-BL-011 | Evidence Pack Library | Create evidence pack templates for ARB, controls, lifecycle, exceptions, resilience, API, cloud, and third-party submissions | Enterprise Architecture / Technology Risk | High | Draft |
| TP-BL-012 | Governance Metrics Catalog | Define KPI/KRI/OKR catalog for Technology Policy operations | Enterprise Architecture | Medium | Not Started |
| TP-BL-013 | Publication Package | Assemble Word-ready publication package for policy, standards, registers, RTM, and appendices | Enterprise Architecture | Critical | Not Started |
| TP-BL-014 | Release Notes | Create release notes for Technology Policy Version 1.0 | Enterprise Architecture | Medium | Not Started |
| TP-BL-015 | Control Validation Workflow | Add repository validation rules for required fields, ID formats, and traceability completeness | Enterprise Architecture / Engineering Enablement | Medium | Not Started |

## Immediate Next Three Actions

1. Expand `ETP-RQ` requirements to cover all Technology Policy domains and three standards.
2. Expand `CTRL` controls to maintain one-to-one or one-to-many coverage against requirements.
3. Expand the RTM to map each requirement and control to regulatory and framework drivers.

## Non-Negotiables

- No standard shall exist without a mapped policy domain.
- No mandatory requirement shall exist without a mapped control objective.
- No control objective shall exist without an evidence source.
- No material architecture decision shall bypass ARB.
- No exception shall be open-ended.
- No lifecycle exception shall be approved without compensating control or retirement path.
