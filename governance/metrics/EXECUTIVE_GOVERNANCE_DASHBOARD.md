# Executive Governance Dashboard

## Document Control

| Field | Value |
|---|---|
| Artifact ID | ETGF-MET-DASH-001 |
| Owner | Head of Enterprise Architecture |
| Executive Owner | CIO |
| Status | Draft |
| Version | 0.1 |
| Review Frequency | Monthly |
| System of Record | GitHub for specification; ServiceNow/Archer for operational data |

## Purpose

The Executive Governance Dashboard provides a concise view of whether the Technology Policy control plane is operating effectively. It is intended for CIO, CTO, CISO, CRO, COO, Internal Audit, and executive technology governance review.

This dashboard is not a vanity metric pack. It is designed to show whether material architecture decisions are governed, evidence exists, exceptions are controlled, lifecycle risk is visible, and regulatory traceability is defensible.

## Dashboard Sections

### 1. Architecture Governance Health

| Metric | Executive Question Answered |
|---|---|
| ARB Throughput | Is ARB reviewing enough material demand to be relevant? |
| ARB Cycle Time | Is governance enabling delivery or creating drag? |
| Material Change Pre-Approval Rate | Are material changes being approved before implementation? |
| Architecture Evidence Completeness | Are decisions supported by evidence? |

### 2. Policy and Control Traceability

| Metric | Executive Question Answered |
|---|---|
| Requirements Traceability Coverage | Can every policy requirement be traced to controls and regulatory drivers? |
| Control Evidence Aging | Are controls supported by current evidence? |
| Governance Reporting Timeliness | Is management oversight operating on schedule? |

### 3. Exception and Waiver Risk

| Metric | Executive Question Answered |
|---|---|
| Open Architecture Exceptions | Where is accepted or unresolved architecture risk accumulating? |
| Waiver Remediation Timeliness | Are temporary deviations actually temporary? |
| Standards Exception Concentration | Which standards are being repeatedly bypassed? |

### 4. Technology Lifecycle and Portfolio Risk

| Metric | Executive Question Answered |
|---|---|
| Technology Lifecycle Risk | What technology risk exists due to sunset, contained, prohibited, or unsupported platforms? |
| EOL/EOS Remediation Progress | Are lifecycle remediation plans moving? |
| Application Portfolio Rationalization Progress | Are redundant or legacy applications being reduced? |
| Capability Mapping Coverage | Are applications and services mapped to business capabilities? |
| CSDM Relationship Completeness | Is the service model operationally usable? |

### 5. Security, Resilience, Third Party, and AI Governance

| Metric | Executive Question Answered |
|---|---|
| Security Architecture Review Coverage | Are material designs receiving security review? |
| API Product Compliance | Are APIs governed as enterprise products? |
| Operational Resilience Coverage | Are critical services recovery-capable and tested? |
| Third Party Architecture Review Coverage | Are vendor/SaaS decisions reviewed before commitment? |
| AI Governance Review Coverage | Are AI use cases governed before production exposure? |

## Executive Scorecard Model

| Rating | Definition |
|---|---|
| Green | Operating within approved tolerance; no executive intervention required |
| Amber | Operating outside preferred range; management action required |
| Red | Material governance, control, or regulatory risk; executive action required |

## Minimum Monthly Report Format

| Domain | Green | Amber | Red | Top Risk | Required Action | Owner | Due Date |
|---|---:|---:|---:|---|---|---|---|
| Architecture Governance |  |  |  |  |  |  |  |
| Control Traceability |  |  |  |  |  |  |  |
| Exceptions / Waivers |  |  |  |  |  |  |  |
| Lifecycle / Portfolio |  |  |  |  |  |  |  |
| Security / Resilience |  |  |  |  |  |  |  |
| Third Party / AI |  |  |  |  |  |  |  |

## Source Systems

| Data Domain | Source System |
|---|---|
| ARB intake and decisions | ServiceNow EA/APM |
| Change records | ServiceNow Change |
| Controls and issues | Archer or ServiceNow IRM |
| Evidence packages | ServiceNow, Archer, SharePoint |
| Applications and lifecycle | ServiceNow APM / ITAM |
| CSDM relationships | ServiceNow CSDM / CMDB |
| Delivery work items | ADO / Jira |
| Source-controlled governance objects | GitHub |

## Non-Negotiable Executive Messages

1. A material technology change without ARB approval is a governance failure.
2. A requirement without a mapped control is not governable.
3. A control without evidence is not audit-ready.
4. An exception without an owner, expiration date, and remediation path is unmanaged risk.
5. Unsupported technology in critical services is an operational resilience issue, not a documentation issue.
6. AI use cases without inventory, ownership, risk review, and approval are not production-ready.

## Monthly Governance Questions

1. What material decisions were approved, rejected, deferred, or approved with conditions?
2. Which standards are creating the most exceptions and why?
3. Which requirements or controls lack evidence?
4. Which applications, services, or technologies create the highest lifecycle risk?
5. Which critical services lack current resilience validation?
6. Which third-party or AI decisions require executive attention?
7. What changed since last month that affects regulatory posture?

## Exit Criteria for Production Dashboard

- Metrics register approved.
- Data owners assigned.
- Source systems confirmed.
- Thresholds approved.
- Dashboard cadence approved.
- Executive governance forum confirmed.
- Initial baseline produced.
- Monthly reporting owner assigned.

## Status

This dashboard specification is a draft control-plane artifact. It becomes production-ready once source-system data ownership and thresholds are formally approved.
