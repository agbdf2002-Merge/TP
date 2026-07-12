# Technology Policy Governance Operating Cadence

## Purpose

This cadence defines the recurring governance rhythm required to operate the published Technology Policy baseline.

The cadence is designed to ensure that ARB decisions, exceptions, controls, evidence, metrics, and release management operate as a management system rather than disconnected activities.

## Operating Forums

| Forum | Frequency | Chair | Primary Purpose | Required Outputs |
|---|---:|---|---|---|
| Architecture Review Board | Weekly or biweekly | Head of Enterprise Architecture | Review material technology change, decisions, standards alignment, exceptions | ADRs, approval decisions, conditions, exception records |
| Technology Policy Control Review | Monthly | Enterprise Architecture / Technology Risk | Review requirements, controls, evidence, RTM, exceptions, and metrics | Monthly control health report |
| Lifecycle Risk Review | Monthly | EA / ITAM / Operations | Review EOL/EOS, tolerated technologies, prohibited technologies, rationalization risks | Lifecycle risk actions |
| Evidence Review | Monthly | Risk / EA / Control Owners | Validate evidence completeness, aging, and audit readiness | Evidence health report |
| Executive Governance Review | Monthly or quarterly | CIO / delegated executive | Review risk, adoption, exception trends, decisions required | Executive dashboard and decisions |
| Release Review | Quarterly | EA Repository Steward | Review baseline changes, backlog, standards updates, and release candidates | Release decision record |

## Required Monthly Artifacts

| Artifact | Owner | Source |
|---|---|---|
| ARB decision log | ARB Coordinator | ADR register / ServiceNow EA/APM |
| Exception and waiver report | EA / Risk | Exception register / IRM |
| Control evidence report | Control Owners / Risk | Evidence library / Archer / ServiceNow IRM |
| Lifecycle risk report | EA / ITAM / Operations | Technology lifecycle register / CMDB / APM |
| RTM health report | EA / Compliance | RTM register |
| Governance metrics dashboard | EA / Risk | Metrics register and systems of record |

## Standard Agenda: Monthly Technology Policy Control Review

1. Review prior actions and open decisions.
2. Review new or changed requirements, controls, and standards.
3. Review ARB activity and material decision trends.
4. Review exception and waiver exposure.
5. Review evidence completeness and aging.
6. Review lifecycle and portfolio risk.
7. Review regulatory traceability and audit readiness.
8. Confirm escalations to executive governance.
9. Confirm backlog updates and change-control actions.

## Standard Agenda: Executive Governance Review

1. Governance health summary.
2. Key risks and decisions required.
3. ARB throughput and material change exposure.
4. Open exceptions and waivers.
5. Lifecycle risk and EOL/EOS exposure.
6. Evidence and control posture.
7. Regulatory and audit readiness.
8. Approved actions, owners, and due dates.

## Escalation Triggers

| Trigger | Escalation Path |
|---|---|
| Material change bypasses ARB | ARB to CIO / Technology Risk |
| Exception exceeds approved expiration | ARB to Risk Governance |
| Control has no evidence for reporting period | Control Owner to Technology Policy Control Review |
| Regulatory mapping gap identified | EA / Compliance to Executive Governance Review |
| Critical technology lacks owner or lifecycle state | EA / ITAM to Lifecycle Risk Review |
| Repeated noncompliance by same domain or platform | ARB to CIO / accountable executive |

## Operating Rules

- Meetings must produce decisions, actions, or documented no-action outcomes.
- Open actions must have an accountable owner and due date.
- Exceptions must not become permanent architecture.
- Metrics must be sourced from governed systems or registers.
- Any substantive baseline change must follow post-publication change control.

## Governance Metrics Reviewed Monthly

- ARB submissions reviewed.
- ARB cycle time.
- Evidence completeness.
- Control evidence aging.
- Open exceptions and waivers.
- Expired exceptions.
- Requirement-to-control coverage.
- Control-to-evidence coverage.
- RTM completeness.
- Lifecycle risk exposure.
- CSDM relationship completeness.
- Standards exceptions by domain.

## Minimum Recordkeeping

Each governance forum must maintain:

- agenda
- attendees
- decisions
- action items
- escalations
- evidence links
- next review date

## Cadence Health Criteria

The cadence is operating effectively when:

- ARB decisions are recorded before implementation.
- exceptions and waivers have active owners and expiration dates.
- control evidence is refreshed on schedule.
- lifecycle risks are visible to executives.
- traceability gaps are identified before audit.
- release backlog is current.

## Bottom Line

The governance cadence converts the Technology Policy baseline into an operating management system.
