# ADO / Jira Workflow Mapping

## Purpose

This document defines how Technology Policy, Enterprise Architecture standards, ARB decisions, controls, evidence, exceptions, and remediation activities become executable backlog work in Azure DevOps or Jira.

## Operating Rule

Architecture governance decisions SHALL be converted into executable delivery backlog items when implementation, remediation, evidence collection, or exception closure is required.

## Work Item Types

| Work Item Type | Purpose | Trigger | Required Parent | Exit Criteria |
|---|---|---|---|---|
| Architecture Review Epic | Coordinate review of material architecture change | Material change intake | Program / Initiative | ARB decision recorded |
| Architecture Requirement Story | Implement a required architecture control or standard | Policy or standard requirement | Architecture Review Epic | Requirement satisfied and evidence linked |
| Architecture Evidence Task | Collect or attach proof of control operation | Control evidence requirement | Requirement Story | Evidence accepted by owner/reviewer |
| ADR Task | Create or update Architecture Decision Record | ARB decision or material design choice | Architecture Review Epic | ADR approved and linked |
| Exception Remediation Story | Remediate an approved exception or waiver | Exception/waiver approval | Architecture Review Epic or Risk Issue | Exception closed or renewed with approval |
| Technology Lifecycle Remediation Story | Remediate EOL/EOS or non-strategic technology risk | Lifecycle review | Portfolio Epic | Lifecycle risk reduced or accepted |
| Application Rationalization Story | Consolidate, retire, or disposition application | APM review | Portfolio Epic | Application disposition approved and tracked |
| Regulatory Traceability Task | Update requirement/control/regulatory mapping | Regulatory or control change | Governance Epic | RTM updated and reviewed |
| Control Remediation Task | Correct control gap or failed test | Control test failure | Risk Issue / Governance Epic | Retest passed or risk accepted |

## Recommended Workflow States

```text
New -> Triage -> In Architecture Review -> Approved for Delivery -> In Progress -> Evidence Review -> Done
```

Exception workflow:

```text
New -> Risk Assessment -> ARB Review -> Approved Exception -> Remediation In Progress -> Evidence Review -> Closed
```

## Required Fields

| Field | Requirement |
|---|---|
| Governance Object ID | Required for all governance-linked work |
| Requirement ID | Required when implementing or remediating `ETP-RQ` objects |
| Control ID | Required for evidence and remediation tasks |
| ARB Decision ID | Required for material change work |
| Exception ID | Required for exception or waiver remediation |
| Evidence ID | Required for evidence collection tasks |
| Regulatory Mapping | Required for regulatory-driven work |
| Owner | Required |
| Due Date | Required for remediation, evidence, and exception work |
| System of Record Link | Required before closure |

## Done Criteria

A work item SHALL NOT be closed unless:

1. Required governance IDs are populated.
2. Required evidence is linked.
3. Owner has accepted the work.
4. ARB decision conditions, if any, are satisfied or explicitly deferred.
5. Control or risk object is updated where applicable.
6. ServiceNow or Archer/IRM object is updated where applicable.

## Tool Boundary

ADO/Jira executes work. It is not the authoritative system for policy, standards, controls, regulatory traceability, or risk acceptance.

| Object | Authoritative System |
|---|---|
| Policy / Standards | GitHub-controlled repository / approved publication library |
| Requirements | GitHub register, synchronized to IRM as needed |
| Controls | Archer / ServiceNow IRM |
| Evidence | Archer / ServiceNow IRM / approved evidence repository |
| Architecture Objects | ServiceNow EA/APM/CSDM |
| Delivery Tasks | ADO / Jira |
| ARB Decisions | ServiceNow EA/Governance workflow plus GitHub ADR where applicable |

## Anti-Patterns

- Closing delivery work without evidence.
- Treating Jira comments as architecture decisions.
- Treating ADO tasks as risk acceptance.
- Allowing material change implementation without ARB decision linkage.
- Using backlog labels as substitutes for control mappings.

## Metrics

| Metric | Purpose |
|---|---|
| Governance-linked work item completeness | Measures whether work items carry required governance IDs |
| Evidence task closure timeliness | Measures evidence collection discipline |
| Exception remediation aging | Measures unresolved architecture risk |
| ARB condition closure rate | Measures whether ARB conditions are executed |
| Control remediation cycle time | Measures time from control gap identification to closure |
