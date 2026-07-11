# Architecture Principles and Solution Patterns Guide

## Purpose

This guide defines how architecture principles and solution patterns are used within the Technology Policy and Enterprise Technology Governance Framework.

Principles are decision rules.
Patterns are reusable implementation paths.
Standards define what is mandatory.
Controls prove that mandatory requirements operated.
Evidence proves the controls and decisions occurred.

## Operating Model

Architecture principles and patterns SHALL be used by:

- Enterprise Architecture
- Solution Architecture
- Security Architecture
- Platform / Cloud Architecture
- Data Architecture
- Product Engineering
- Technology Operations
- Technology Risk
- ARB reviewers

## Principle Hierarchy

| Level | Object | Purpose |
|---|---|---|
| Level 1 | Category | Groups related architecture concerns |
| Level 2 | Principle | Defines a durable decision rule |
| Level 3 | Solution Pattern | Provides reusable approved implementation path |
| Level 4 | Practice | Defines execution behavior, evidence, and operating expectations |

## Core Principles

| Principle | Plain-English Intent |
|---|---|
| Policy Governs Standards Implement Procedures Execute | Stop governance ambiguity |
| ARB Before Material Change | Prevent late or bypassed architecture decisions |
| One Meaning of Data | Reduce conflicting data definitions and reporting risk |
| APIs Are Products | Treat integration as a managed reusable product capability |
| Secure By Design | Build security into design, not after the fact |
| Resilient By Design | Design for availability, recovery, continuity, and supportability |
| Cloud With Guardrails | Use controlled cloud patterns, not unmanaged cloud adoption |
| Buy Before Build But Do Not Buy Blind | Prefer leverage, but validate risk and fit before buying |
| Design For Observability | Make production behavior visible and supportable |
| Technology Lifecycle Is Managed Risk | Treat lifecycle debt as explicit risk |
| Capability First Architecture | Anchor technology decisions to business capability |
| Evidence Or It Did Not Happen | Preserve decision and control proof in systems of record |

## Pattern Usage in ARB

ARB SHALL use approved solution patterns to determine whether a submission is:

1. Aligned to Technology Policy
2. Aligned to Enterprise Architecture standards
3. Ready for implementation
4. Missing required evidence
5. Creating unacceptable risk
6. Requiring exception or waiver approval

## Pattern-to-Evidence Rule

Every approved solution pattern SHALL define:

- required inputs
- required outputs
- evidence expectations
- related controls
- related standards
- ownership
- applicability criteria

## Required ARB Checks

ARB reviewers SHALL verify:

- business capability mapping exists
- architecture decision record exists when required
- data classification is completed
- security design review is completed
- resilience requirements are defined
- API/integration contracts exist where relevant
- lifecycle status is known
- third-party risk review is completed where relevant
- evidence pack is attached
- exceptions/waivers are time-bound and risk accepted

## Anti-Patterns

The following are prohibited without approved exception:

- material implementation before ARB decision
- undocumented architecture decisions
- unmanaged point-to-point integrations
- APIs without product owners
- systems without data classification
- unsupported technology without remediation plan
- production services without observability
- cloud workloads outside approved guardrails
- permanent exceptions without expiration
- application onboarding without capability and service mapping

## Systems of Record

| Object | System of Record |
|---|---|
| Source standards and schemas | GitHub |
| Architecture objects | ServiceNow EA/APM |
| Services and configuration relationships | ServiceNow CSDM/CMDB |
| Controls, risks, issues, exceptions | Archer / ServiceNow IRM |
| Engineering remediation tasks | ADO / Jira |
| Evidence packages | ServiceNow / Archer / approved document repository |

## Success Metrics

| Metric | Target Direction |
|---|---|
| ARB submissions using approved pattern | Increase |
| Architecture decisions with complete evidence | Increase |
| Exceptions past expiration | Decrease |
| Unmapped applications/services | Decrease |
| Unsupported technology without remediation | Decrease |
| APIs without owners/contracts | Decrease |
| Critical services without observability | Decrease |

## Bottom Line

Architecture principles without patterns are slogans.
Patterns without controls are suggestions.
Controls without evidence are theater.

This framework makes all four operate as one governance system.
