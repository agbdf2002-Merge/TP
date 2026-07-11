# Enterprise Object Model

## Purpose

The Enterprise Object Model defines the governed objects that connect policy, standards, requirements, controls, evidence, regulatory obligations, architecture decisions, business capabilities, applications, technology services, and systems of record.

## Canonical Relationship Chain

```text
Enterprise Policy
→ Requirement
→ Principle
→ Standard
→ Control
→ Evidence
→ Regulation
→ System of Record
→ Architecture Object
→ Application
→ Technology Service
→ Business Capability
```

## Core Object Types

| Object Type | Description | Example ID |
|---|---|---|
| Policy | Mandatory governance document | ETP-001 |
| Standard | Implementation requirement for a policy domain | EA-STD-001 |
| Requirement | Specific mandatory policy statement | ETP-RQ-0001 |
| Control | Control objective validating requirement operation | CTRL-001 |
| Evidence | Artifact proving control operation | EVD-001 |
| Principle | Stable architecture decision rule | PR-001 |
| Pattern | Reusable architecture solution pattern | PAT-001 |
| Exception | Approved deviation from a standard or control | EXC-001 |
| Architecture Decision | ARB decision record | ADR-001 |
| Capability | Business capability object | CAP-001 |
| Application | Application portfolio object | APP-001 |
| Service | Business or technology service | SVC-001 |
| Technology | Technology product or platform | TECH-001 |

## System Alignment

| Object | Primary System of Record |
|---|---|
| Policy and standards | GitHub / SharePoint |
| Requirements and controls | Archer / ServiceNow IRM |
| Applications | ServiceNow APM |
| Services and CIs | ServiceNow CSDM / CMDB |
| Architecture decisions | ServiceNow EA/APM / GitHub |
| Exceptions and waivers | ServiceNow / Archer |
| Engineering work | Azure DevOps / Jira |
