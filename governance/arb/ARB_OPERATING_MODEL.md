# Architecture Review Board Operating Model

## Purpose

The Architecture Review Board is the enterprise decision authority for material architecture decisions, technology standards compliance, architecture exceptions, technology lifecycle risk, and architecture alignment to the Enterprise Technology Governance Framework.

## Governing Principle

Community informs. Workforce enables. ARB decides. Operations execute.

## Scope

ARB review is required for material changes that affect:

- Business capability alignment
- Application portfolio and lifecycle state
- Technology standards compliance
- Security architecture
- Data protection or privacy posture
- Cloud, infrastructure, network, or platform architecture
- API, integration, or software engineering patterns
- Operational resilience or recoverability
- Third-party technology concentration or dependency risk
- AI, model, or emerging technology use
- CMDB, business service, or technical service alignment

## Decision Types

| Decision Type | Description | Output |
|---|---|---|
| Architecture Approval | Approval of a proposed material architecture | ADR and evidence pack |
| Conditional Approval | Approval with required remediation, controls, or milestones | ADR, conditions, due dates |
| Standard Exception | Approved deviation from a required standard | Exception record |
| Waiver | Time-bound deferral of a requirement or control | Waiver record |
| Rejection | Decision that proposal does not meet enterprise requirements | ADR with rationale |
| Deferral | More analysis, evidence, or stakeholder review required | Deferred decision record |

## Required Inputs

| Input | Required | Notes |
|---|---|---|
| Architecture Decision Record | Yes | Required for all material decisions |
| Architecture Evidence Pack | Yes | Required for approval or exception |
| Capability mapping | Yes | Must map to business capability or service |
| Application/service mapping | Conditional | Required when application or service impacted |
| Security review | Yes | Required for material technology change |
| Data classification | Conditional | Required where data is created, moved, stored, processed, or exposed |
| Resilience assessment | Conditional | Required for production or customer-impacting services |
| Third-party assessment | Conditional | Required for vendor/SaaS/managed service dependency |
| Control mapping | Yes | Requirement-to-control evidence required |
| Exception/waiver record | Conditional | Required where standards are not met |

## Review Gates

| Gate | Purpose | Decision Authority |
|---|---|---|
| Intake Triage | Determine materiality and required review path | EA Intake Lead |
| Pre-ARB Review | Validate evidence completeness and standards alignment | Domain Architects |
| ARB Decision | Approve, reject, defer, or condition architecture decision | ARB |
| Post-Decision Tracking | Track conditions, exceptions, waivers, and evidence | EA Governance Lead |
| Implementation Confirmation | Confirm architecture decision was implemented as approved | EA / Delivery / Operations |

## ARB Decision Criteria

A proposal should be approved only when it demonstrates:

1. Alignment to business capability and strategic direction.
2. Alignment to approved standards and patterns.
3. Clear application/service/technology ownership.
4. Security and data protection by design.
5. Resilience, recovery, and operational supportability.
6. Lifecycle viability and supportability.
7. Third-party risk review where applicable.
8. Integration with ServiceNow CSDM/CMDB where applicable.
9. Traceability to requirements, controls, and evidence.
10. Defined exception or waiver path where standards cannot be met.

## ARB Outputs

| Output | System of Record |
|---|---|
| ADR | GitHub / ServiceNow EA/APM |
| Evidence Pack | ServiceNow / Archer / SharePoint |
| Exception Record | ServiceNow / Archer |
| Waiver Record | ServiceNow / Archer |
| Application/Service Updates | ServiceNow APM/CSDM/CMDB |
| Risk or Issue Record | Archer / ServiceNow IRM |
| Engineering Follow-up | Azure DevOps / Jira |

## Metrics

| Metric | Purpose |
|---|---|
| ARB submission volume | Demand and throughput |
| Approval rate | Quality of intake and design alignment |
| Conditional approval rate | Standards and evidence maturity |
| Exception count | Standards non-compliance and lifecycle risk |
| Waiver aging | Residual risk exposure |
| Evidence completeness | Audit readiness |
| Time to decision | Governance efficiency |
| Post-approval variance | Delivery conformance |

## Non-Negotiables

- ARB approval shall occur before material technology change implementation.
- Exceptions shall be time-bound, risk-accepted, and tracked.
- Waivers shall not become permanent architecture patterns.
- Architecture decisions shall be evidence-backed.
- Controls shall map to requirements and regulatory drivers.
- ServiceNow and Archer mappings shall be maintained for audit and operational execution.
