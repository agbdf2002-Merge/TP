# Technology Policy Repository Operating Index

## Purpose

This index provides the operating map for the Technology Policy and Enterprise Technology Governance Framework content in this repository.

This repository is intended to function as the controlled source for:

- Enterprise Technology Policy
- Enterprise Architecture standards
- Technology Governance standards
- Technology Lifecycle standards
- master document, requirement, and control registers
- regulatory traceability
- ARB decisioning
- exception and waiver governance
- architecture evidence packs
- enterprise technology taxonomy
- enterprise object model
- future ServiceNow / Archer / IRM implementation mappings

## Governing Rule

Policy governs. Standards implement. Procedures execute. Engineering standards configure. Evidence proves operation.

## Operating Model

Community informs. Workforce enables. ARB decides. Operations execute.

## Repository Navigation

| Area | Path | Purpose |
|---|---|---|
| Technology Policy Bootstrap | `governance/technology-policy/TECHNOLOGY_POLICY_BOOTSTRAP.md` | Parent framework and governance construct |
| Repository Index | `governance/technology-policy/TECHNOLOGY_POLICY_REPOSITORY_INDEX.md` | Navigation and operating map |
| Enterprise Architecture Standard | `governance/standards/ENTERPRISE_ARCHITECTURE_STANDARD.md` | EA implementation standard |
| Technology Governance Standard | `governance/standards/TECHNOLOGY_GOVERNANCE_STANDARD.md` | Governance implementation standard |
| Technology Lifecycle Standard | `governance/standards/TECHNOLOGY_LIFECYCLE_STANDARD.md` | Technology lifecycle implementation standard |
| EA Standards Register | `governance/standards/ENTERPRISE_ARCHITECTURE_STANDARDS_REGISTER.md` | Standards inventory and control mapping |
| Master Document Register | `registers/master/master_document_register.csv` | Controlled artifact inventory |
| Master Requirements Register | `registers/master/master_requirements_register.csv` | Mandatory policy requirements |
| Master Control Register | `registers/master/master_control_register.csv` | Control objectives and evidence mapping |
| Regulatory Traceability Matrix | `registers/traceability/regulatory_traceability_matrix.csv` | Requirement/control/regulatory mapping |
| RTM Documentation | `governance/traceability/REGULATORY_TRACEABILITY_MATRIX.md` | RTM operating instructions |
| ARB Operating Model | `governance/arb/ARB_OPERATING_MODEL.md` | ARB scope, gates, decision rights, and outputs |
| Exception and Waiver Standard | `governance/exceptions/EXCEPTION_AND_WAIVER_STANDARD.md` | Exception/waiver rules and escalation |
| Exception/Waiver Register | `registers/governance/exception_waiver_register.csv` | Exception/waiver inventory |
| ADR Template | `governance/templates/architecture_decision_record_template.md` | ARB decision record template |
| Evidence Pack Template | `governance/templates/architecture_evidence_pack_template.md` | Audit evidence package template |
| Governance Object Schema | `schemas/json/technology-governance-object.schema.json` | Canonical object schema |
| YAML Governance Object Template | `schemas/yaml/technology-governance-object.template.yaml` | Machine-readable object template |
| Enterprise Technology Taxonomy | `knowledge/taxonomy/enterprise_technology_taxonomy_seed.md` | Technology domain taxonomy seed |
| Enterprise Object Model | `knowledge/object-model/enterprise_object_model.md` | Governance object model |
| Control Plane Overview | `knowledge/control-plane/control_plane_overview.md` | Requirements/controls/evidence operating model |
| Release Package Index | `releases/technology-policy/TP_RELEASE_PACKAGE_INDEX.md` | Release package inventory |

## Minimum Traceability Rule

Every mandatory requirement shall map to:

1. A policy domain.
2. A responsible owner.
3. A standard or control objective.
4. An evidence source.
5. A system of record.
6. A regulatory or framework driver, unless explicitly classified as an internal management practice.

## Systems of Record

| Function | System of Record |
|---|---|
| Architecture objects | ServiceNow EA / APM |
| Business and technology services | ServiceNow CSDM / CMDB |
| Controls and issues | Archer / ServiceNow IRM |
| Engineering work | Azure DevOps / Jira |
| Evidence packages | ServiceNow / Archer / SharePoint |
| Source-controlled standards | GitHub |

## Next Required Build Packages

| Package | Output | Status |
|---|---|---|
| Requirements Expansion | `ETP-RQ-0001+` full register | Pending |
| Controls Expansion | `CTRL-001+` full register | Pending |
| ServiceNow Object Mapping | EA/APM/CSDM mapping | Pending |
| Archer/IRM Object Mapping | Risk/control/evidence mapping | Pending |
| Publication Package | Word-ready content set | Pending |
| Governance Metrics | KPI/KRI/OKR catalog | Pending |
