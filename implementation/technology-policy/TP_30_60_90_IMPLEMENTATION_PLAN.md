# Technology Policy 30/60/90 Implementation Plan

## Purpose

This plan converts the final Technology Policy publication baseline into an executable implementation roadmap.

The objective is not to rewrite the policy. The objective is to operationalize it through ownership, intake, controls, evidence, reporting, and platform alignment.

## Operating Assumptions

- Final publication baseline is closed.
- Substantive content changes require post-publication change control.
- Platform import validation and dry-runs are separately dispositioned.
- EA owns the governance source and architecture control plane.
- Operations, Risk, Security, Engineering, and platform owners execute their assigned lanes.

## Day 0 to Day 30: Stabilize and Communicate

### Objectives

- Establish the operating baseline.
- Communicate decision rights.
- Confirm ownership for registers, controls, evidence, and ARB operations.
- Prevent uncontrolled drift.

### Key Activities

| Workstream | Activity | Owner | Output |
|---|---|---|---|
| Repository Governance | Confirm GitHub as source-controlled governance repository | Enterprise Architecture | Repository stewardship model |
| Publication | Distribute final baseline to document-management and stakeholder channels | EA / OCIO | Published baseline package |
| ARB | Confirm ARB scope, intake triggers, required evidence, and decision states | Enterprise Architecture | ARB operating calendar |
| Registers | Assign owners for document, requirement, control, evidence, and RTM registers | Enterprise Architecture / Risk | Register owner matrix |
| Evidence | Define evidence collection cadence and storage model | Risk / EA / Platform Owners | Evidence operating model |
| Communications | Issue stakeholder communication and implementation expectations | CIO / EA | Implementation communication |

### Exit Criteria

- Baseline communication completed.
- Register owners assigned.
- ARB intake rules confirmed.
- Change-control rules active.
- First governance reporting cycle scheduled.

## Day 31 to Day 60: Operationalize Controls

### Objectives

- Move from documented controls to operating controls.
- Begin evidence capture.
- Establish platform implementation sequencing.
- Start exception and waiver governance.

### Key Activities

| Workstream | Activity | Owner | Output |
|---|---|---|---|
| Controls | Validate `CTRL-001` through `CTRL-032` against operating teams | EA / Risk | Control ownership confirmation |
| Evidence | Begin evidence collection for priority controls | Control Owners | Evidence package set |
| ServiceNow | Prepare object mapping and load sequencing for EA/APM/CSDM/CMDB/IRM | ServiceNow Platform Owner / EA | Import readiness decision |
| Archer / IRM | Prepare policy, requirement, control, evidence, risk, and exception object mapping | Risk Platform Owner | IRM mapping decision |
| ADO / Jira | Confirm work item types and workflow states for architecture governance execution | Engineering Enablement | Delivery workflow mapping |
| Exceptions | Start exception/waiver review process | ARB / Risk | Exception register activation |

### Exit Criteria

- Control owners validated.
- Evidence collection started.
- Exception register active.
- Platform import decisions tracked.
- First metrics report drafted.

## Day 61 to Day 90: Measure and Enforce

### Objectives

- Establish governance reporting rhythm.
- Begin enforcing ARB gates and evidence expectations.
- Prepare the next release backlog.
- Identify noncompliance and adoption risks.

### Key Activities

| Workstream | Activity | Owner | Output |
|---|---|---|---|
| Metrics | Produce first monthly governance dashboard | EA / Risk | Executive dashboard |
| ARB | Enforce material change review and decision record creation | ARB | ARB decision log |
| Lifecycle | Identify lifecycle risk hotspots and EOL/EOS exposure | EA / ITAM / Operations | Lifecycle risk report |
| Evidence | Score evidence completeness and aging | Risk / EA | Evidence health report |
| RTM | Validate regulatory traceability completeness | EA / Compliance | RTM validation record |
| Release Governance | Prepare `TP-vNext` backlog | EA | Release backlog |

### Exit Criteria

- Governance dashboard operational.
- ARB evidence-pack process active.
- Lifecycle risk reporting started.
- Release backlog established.
- Noncompliance issues tracked.

## 90-Day Success Measures

| Measure | Target |
|---|---|
| Register owner assignment | 100% |
| Control owner confirmation | 100% |
| ARB intake operating cadence | Active |
| Evidence collection initiated | Priority controls |
| Exception register | Active |
| Governance dashboard | First monthly version issued |
| Change-control process | Active |
| Release backlog | Created |

## Material Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Platform implementation lags governance publication | Controls exist on paper only | Track as implementation backlog |
| Register ownership is unclear | Traceability decay | Assign named functional owners |
| Evidence is stored inconsistently | Audit defensibility weakens | Use evidence library and package guide |
| ARB gate is bypassed | Material risk enters production | Enforce intake trigger and exception rules |
| Standards are treated as optional | Governance erosion | Tie to controls, metrics, and waiver process |

## Governance Rule

Publication is complete. Implementation is now the control objective.

Future changes to the baseline must follow post-publication change control.
