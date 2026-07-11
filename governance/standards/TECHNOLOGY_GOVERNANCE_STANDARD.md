# Technology Governance Standard

## Document Control

| Field | Value |
|---|---|
| Document ID | ETS-002 |
| Title | Technology Governance Standard |
| Parent Policy | Enterprise Technology Policy |
| Owner | Head of Enterprise Architecture |
| Executive Owner | Chief Information Officer |
| Governing Body | Architecture Review Board |
| Status | Draft |
| Version | 0.1 |
| Review Frequency | Annual or upon material change |

## 1. Purpose

This standard defines the governance operating model used to implement the Enterprise Technology Policy. It establishes decision rights, document hierarchy, control-plane registers, evidence expectations, exception handling, and traceability requirements.

The standard ensures technology governance is consistent, auditable, risk-based, and aligned to regulatory expectations for financial institutions.

## 2. Scope

This standard applies to:

- enterprise technology policies;
- technology and architecture standards;
- architecture principles;
- technology requirements;
- control objectives;
- regulatory traceability mappings;
- architecture decisions;
- exceptions and waivers;
- evidence packs;
- governance metrics;
- ServiceNow, Archer, Azure DevOps, Jira, and source-control governance objects.

## 3. Governance Hierarchy

The Bank SHALL maintain the following technology governance hierarchy:

| Level | Object | Purpose |
|---|---|---|
| 1 | Policy | Establishes mandatory enterprise-level governance expectations. |
| 2 | Standard | Defines implementation requirements for policy domains. |
| 3 | Procedure | Defines step-by-step execution activities. |
| 4 | Pattern / Reference Architecture | Defines reusable approved implementation guidance. |
| 5 | Control | Defines objective used to validate requirement operation. |
| 6 | Evidence | Proves control operation and decision compliance. |

Policy governs. Standards implement. Procedures execute. Controls validate. Evidence proves.

## 4. Governance Bodies

The Bank SHALL maintain defined governance bodies for technology oversight.

| Body | Role |
|---|---|
| Architecture Review Board | Architecture decisioning, standards alignment, material change review, exceptions, and waivers. |
| Technology Risk Governance | Technology risk, control issues, risk acceptance, and audit coordination. |
| Change Advisory Board | Implementation change readiness, operational scheduling, and change execution governance. |
| AI Governance Body | AI use-case governance, model risk alignment, and AI control oversight. |
| Data Governance Body | Data ownership, classification, privacy, retention, and lineage governance. |

ARB and CAB SHALL remain separate gates. ARB SHALL evaluate architecture fitness before material implementation change proceeds to CAB or equivalent change execution governance.

## 5. Decision Rights

Decision rights SHALL be documented for policy, standard, architecture, control, risk, exception, and implementation decisions.

| Decision Type | Decision Authority |
|---|---|
| Technology Policy approval | Designated executive governance body |
| Architecture standard approval | ARB or delegated architecture governance authority |
| Material architecture approval | ARB |
| Technology lifecycle exception | ARB with risk escalation where required |
| Control issue acceptance | Technology Risk Governance / designated risk authority |
| Change implementation approval | CAB / change governance |
| AI use-case approval | AI Governance Body |
| Data classification decision | Data Governance Body |

## 6. Control-Plane Registers

The Bank SHALL maintain the following master registers:

| Register | Purpose | Owner |
|---|---|---|
| Master Document Register | Controlled document inventory | Enterprise Architecture |
| Master Requirements Register | Mandatory policy and standard requirements | Enterprise Architecture |
| Master Control Register | Control objectives mapped to requirements | Technology Risk / Enterprise Architecture |
| Regulatory Traceability Matrix | Mapping of requirements and controls to regulatory/framework drivers | Enterprise Architecture / Risk |
| Exception and Waiver Register | Approved deviations and remediation obligations | Enterprise Architecture |
| Architecture Decision Register | ARB decision history | Enterprise Architecture |
| Enterprise Technology Taxonomy | Common governance language and object model | Enterprise Architecture |

## 7. Minimum Traceability Requirements

Each requirement SHALL map to:

- one or more policy domains;
- a responsible owner;
- one or more control objectives;
- an evidence source;
- a system of record;
- one or more regulatory or framework references, unless classified as internal management practice;
- review frequency;
- lifecycle status.

Each control SHALL map to:

- one or more requirements;
- a control owner;
- control type;
- control frequency;
- evidence source;
- system of record;
- audit method;
- regulatory or framework reference;
- testing status.

## 8. Systems of Record

The Bank SHALL identify authoritative systems of record for governance objects.

| Governance Object | System of Record |
|---|---|
| Policies and standards | GitHub / document repository |
| Requirements | Master Requirements Register |
| Controls | Archer / ServiceNow IRM / Master Control Register |
| Architecture decisions | GitHub / ServiceNow EA |
| Architecture objects | ServiceNow EA/APM |
| Business services | ServiceNow CSDM |
| Technology services | ServiceNow CSDM / CMDB |
| Applications | ServiceNow APM / CMDB |
| Risks and issues | Archer / ServiceNow IRM |
| Engineering backlog | Azure DevOps / Jira |
| Evidence packs | ServiceNow / Archer / approved repository |

## 9. Governance Workflow

Technology governance SHALL follow this minimum workflow for material technology change:

1. Intake is created.
2. Business capability and service impact are identified.
3. Architecture impact assessment is completed.
4. Security, data, resilience, and third-party impacts are assessed.
5. ARB review is conducted when required.
6. ARB decision and conditions are documented.
7. Exceptions or waivers are documented when required.
8. Controls and evidence requirements are mapped.
9. Implementation proceeds through change governance.
10. Evidence is retained and linked to the appropriate control-plane objects.

## 10. Evidence Management

Evidence SHALL be complete, dated, attributable, and retrievable.

Evidence SHALL identify:

- evidence owner;
- evidence source;
- related requirement;
- related control;
- related architecture decision;
- review date;
- approval status;
- retention requirement.

Evidence SHALL NOT be considered valid when it is incomplete, unauthenticated, materially outdated, or disconnected from the relevant requirement and control.

## 11. Exception and Waiver Governance

Exceptions and waivers SHALL be documented in the approved register and SHALL include:

- affected policy, standard, requirement, and control;
- business justification;
- risk impact;
- compensating controls;
- accountable owner;
- approval authority;
- expiration date;
- remediation plan;
- review cadence.

Expired exceptions SHALL be escalated.

## 12. Governance Metrics

The Bank SHALL maintain and report governance metrics, including:

- standards coverage;
- requirements coverage;
- control mapping completeness;
- evidence completeness;
- open exception count;
- exception aging;
- ARB decision cycle time;
- open architecture risks;
- lifecycle remediation progress;
- audit findings related to technology governance;
- regulatory traceability coverage.

## 13. Regulatory and Framework Alignment

This standard supports alignment to:

- FFIEC Management;
- FFIEC Architecture, Infrastructure, and Operations;
- OCC Heightened Standards;
- Federal Reserve operational resilience expectations;
- FDIC supervisory expectations;
- Interagency Third-Party Risk Management Guidance;
- GLBA Safeguards;
- NIST CSF 2.0;
- NIST SP 800-53;
- CIS Controls;
- COBIT;
- ISO/IEC 27001;
- TOGAF;
- BIAN;
- ServiceNow CSDM.

## 14. Enforcement

Technology governance non-compliance SHALL be remediated, risk accepted by the appropriate authority, or escalated through the approved governance model.
