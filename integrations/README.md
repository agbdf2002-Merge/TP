# Technology Policy Integration Layer

## Purpose

This folder defines import and integration templates for operationalizing the Technology Policy control plane across enterprise systems of record.

The intent is not to make GitHub the runtime GRC system. GitHub is the source-controlled engineering repository for policy, standards, schemas, and seed registers. Runtime execution belongs in ServiceNow, Archer/IRM, ADO/Jira, and approved evidence repositories.

## Integration Principles

1. GitHub is the authoritative source for version-controlled policy engineering artifacts.
2. ServiceNow is the operational source for architecture objects, EA/APM objects, CSDM/service relationships, CMDB alignment, and architecture workflow where implemented.
3. Archer or ServiceNow IRM is the authoritative source for risk, controls, issues, findings, regulatory mappings, attestations, and evidence testing.
4. ADO/Jira is the execution source for delivery backlog, remediation tasks, evidence collection work, and implementation actions.
5. No system shall create unmanaged policy, standard, requirement, or control IDs outside the canonical ID model.
6. Exceptions and waivers shall remain time-bound, risk-rated, approved, and traceable to affected requirements and controls.
7. Architecture decisions shall be documented through ADRs and linked to ARB outcomes when material.

## Included Templates

| Folder | Artifact | Purpose |
|---|---|---|
| `servicenow/` | `servicenow_import_templates.csv` | Defines ServiceNow EA/APM/CSDM/CMDB/IRM import object templates. |
| `archer/` | `archer_irm_import_templates.csv` | Defines Archer/IRM policy, requirement, control, evidence, risk, issue, and regulatory citation objects. |
| `ado-jira/` | `ado_jira_work_item_templates.csv` | Defines delivery work item structures for architecture reviews, controls, evidence, exceptions, lifecycle remediation, and traceability. |

## Source-of-Truth Model

| Object Type | Authoritative Source | Secondary/Consumer Systems |
|---|---|---|
| Policy / Standard Text | GitHub | SharePoint, Archer, ServiceNow Knowledge |
| Requirement Register | GitHub seed, Archer/IRM runtime | ServiceNow, ADO/Jira |
| Control Register | Archer/IRM runtime | GitHub seed, ServiceNow IRM |
| Architecture Object | ServiceNow EA/APM | GitHub reference exports |
| Business Capability | ServiceNow CSDM / EA Taxonomy | GitHub taxonomy seed |
| Application Portfolio | ServiceNow APM | Archer/IRM, ADO/Jira |
| CMDB CI | ServiceNow CMDB | ServiceNow CSDM, Archer/IRM |
| Exception / Waiver | Archer/IRM or ServiceNow IRM | GitHub register export, ADO/Jira remediation |
| Evidence | Archer/IRM or approved evidence repository | ADO/Jira tasks, ServiceNow records |
| Delivery Work Item | ADO/Jira | ServiceNow, Archer/IRM references |

## Minimum Integration Rule

Every implemented integration shall preserve the following keys:

- Policy ID
- Standard ID
- Requirement ID
- Control ID
- Evidence ID
- Architecture Object ID
- Application ID
- Service ID
- Capability ID
- Exception ID, when applicable

## Current Status

Status: Seeded

Next steps:

1. Convert CSV templates into actual platform import formats.
2. Validate ServiceNow object/table names against the deployed modules.
3. Validate Archer application/object names against the bank's Archer taxonomy.
4. Define synchronization pattern between Archer and ServiceNow IRM.
5. Create sample records for each object type.
6. Add automated CSV schema validation in GitHub Actions.
