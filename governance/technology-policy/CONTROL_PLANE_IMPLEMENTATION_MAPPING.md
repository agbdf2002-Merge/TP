# Technology Policy Control Plane Implementation Mapping

## Purpose

This document defines how the Technology Policy control plane shall be implemented across the target systems of record.

The operating intent is simple: GitHub stores the governed source artifacts; ServiceNow operationalizes architecture, application, service, CMDB, and workflow records; Archer or ServiceNow IRM manages risk, controls, issues, and evidence; ADO/Jira connects requirements and controls to engineering execution.

## Core Rule

Policy governs. Standards implement. Procedures execute. Controls prove. Evidence sustains. ARB decides.

## System-of-Record Allocation

| Control Plane Object | Primary System of Record | Secondary System | Notes |
|---|---|---|---|
| Enterprise Technology Policy | GitHub / SharePoint | ServiceNow Knowledge | GitHub is engineering source; SharePoint may be publication location. |
| Standards | GitHub | ServiceNow Knowledge | Standards remain version controlled. |
| Requirements | GitHub / ServiceNow | Archer / IRM | Requirements map to controls and evidence. |
| Controls | Archer / ServiceNow IRM | GitHub | Controls are testable objects with owner, evidence, and audit method. |
| Regulatory Traceability | Archer / GitHub | ServiceNow IRM | RTM must map regulation to requirement to control. |
| Architecture Decisions | ServiceNow EA/APM | GitHub | ADR templates may be stored in GitHub; decisions should become operational records. |
| ARB Submissions | ServiceNow EA/APM | Jira / ADO | Intake and workflow should be executed in ServiceNow where possible. |
| Exceptions and Waivers | ServiceNow / Archer | GitHub | Exceptions must be time-bound and risk accepted. |
| Applications | ServiceNow APM | CMDB | Application records must map to owners and lifecycle state. |
| Business Capabilities | ServiceNow EA/APM | BIAN mapping repository | Capability alignment enables business traceability. |
| Business Services | ServiceNow CSDM | CMDB | Required for service and dependency alignment. |
| Technology Services | ServiceNow CSDM | CMDB | Required for operational ownership and service mapping. |
| Configuration Items | ServiceNow CMDB | Discovery / Service Graph | CMDB execution remains operational, architecture intent informs relationships. |
| Engineering Work Items | ADO / Jira | GitHub | Work items should reference requirement/control IDs. |
| Evidence Packs | ServiceNow / Archer | GitHub / SharePoint | Evidence should be structured and reusable for audit. |
| Metrics and Reporting | ServiceNow / Archer / Power BI | GitHub | Dashboards should consume register/control-plane data. |

## Minimum Object Relationships

Every material technology change shall establish the following minimum traceability chain:

```text
Business Capability
  -> Business Service
    -> Application / Platform / Product
      -> Technology Service
        -> Architecture Decision
          -> Policy Requirement
            -> Control Objective
              -> Evidence Pack
                -> Regulatory / Framework Reference
```

## ServiceNow Implementation View

| ETGF Object | ServiceNow Target Object / Module | Required Fields |
|---|---|---|
| Business Capability | EA / APM capability model | ID, name, owner, domain, criticality |
| Application | APM application record | owner, lifecycle, criticality, business capability, technology stack |
| Technology Service | CSDM technology service | owner, support group, related application, related CI |
| Business Service | CSDM business service | business owner, service criticality, related applications |
| Architecture Decision | EA/APM decision or demand record | ADR ID, decision, conditions, ARB date, evidence link |
| ARB Submission | Demand / EA workflow | requester, scope, impacted systems, decision, conditions |
| Exception / Waiver | IRM issue/risk or custom governance object | exception ID, expiry, risk owner, compensating control |
| Evidence Pack | Attachment / knowledge / IRM evidence object | evidence ID, mapped controls, owner, date, validation status |
| CMDB Relationship | CMDB relationship table | application-service-CI mapping and relationship type |

## Archer / IRM Implementation View

| ETGF Object | Archer / IRM Target | Required Fields |
|---|---|---|
| Requirement | Requirement or obligation object | requirement ID, policy domain, owner, related regulation |
| Control | Control object | control ID, objective, owner, frequency, type, evidence |
| Risk | Risk object | inherent risk, residual risk, risk owner, treatment |
| Issue | Issue object | remediation plan, due date, owner, status |
| Exception | Exception object | risk acceptance, expiry, compensating controls |
| Evidence | Evidence object | mapped control, testing date, artifact link, validator |
| Regulatory Mapping | Compliance mapping object | regulation, citation, requirement, control |

## ADO / Jira Implementation View

Engineering work items shall include the following fields or tags where applicable:

| Field / Tag | Requirement |
|---|---|
| `ETP-RQ-ID` | Link to one or more policy requirements. |
| `CTRL-ID` | Link to one or more control objectives. |
| `ARB-ID` | Link to ARB submission or decision. |
| `ADR-ID` | Link to architecture decision record. |
| `Exception-ID` | Link to approved exception or waiver, if applicable. |
| `Evidence-Pack-ID` | Link to evidence pack for audit and review. |
| `Lifecycle-State` | Technology or application lifecycle state. |
| `Business-Capability` | Business capability impacted by the work item. |

## GitHub Implementation View

GitHub is the source-controlled engineering repository for:

- policy source files
- standards source files
- schemas
- register CSVs
- traceability seed files
- templates
- release package indexes
- repository validation workflows

GitHub shall not be the sole system of record for operational risk acceptance, control execution, or CMDB state.

## Governance Workflow

1. Business or technology demand is initiated.
2. Demand is mapped to business capability and application/platform/service records.
3. Materiality is assessed.
4. If material, ARB review is required before implementation.
5. Requirements and controls are mapped.
6. Evidence pack is created.
7. Exceptions or waivers are documented if standards cannot be met.
8. Approved architecture decision is linked to delivery work items.
9. Implementation evidence is attached to the control/evidence record.
10. Metrics are reported through governance dashboards.

## Non-Negotiables

- Material changes require ARB before implementation.
- Exceptions and waivers must expire.
- Requirements must map to controls.
- Controls must map to evidence.
- Architecture objects must map to business capability and service context.
- ServiceNow and Archer/IRM should be implementation systems, not after-the-fact evidence dumping grounds.

## Current Status

Status: Draft / Seeded

Next enhancement: create system-specific import templates for ServiceNow EA/APM/CSDM, Archer/IRM controls, and ADO/Jira work item tagging.
