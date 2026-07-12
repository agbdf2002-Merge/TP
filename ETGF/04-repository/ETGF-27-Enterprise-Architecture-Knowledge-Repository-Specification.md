# ETGF-27 – Enterprise Architecture Knowledge Repository Specification

## Purpose and Scope

This specification defines the authoritative enterprise architecture knowledge repository for the Enterprise Technology Governance Framework (ETGF). It binds policy, standards, requirements, controls, architecture decisions, technology lifecycle records, services, applications, data, evidence, risks, exceptions, and implementation work into one governed information model.

This specification does not redesign governance bodies or decision rights. It operationalizes the approved ETGF architecture and establishes repository controls required for sustained use.

## Repository Governance

- Enterprise Architecture owns the repository operating model, taxonomy, metadata standard, and architecture content quality.
- Object owners remain accountable for source-record accuracy and lifecycle maintenance.
- Approved artifacts shall be version controlled, traceable, searchable, and retained in an authoritative repository.
- Policy governs, standards implement, procedures execute, and evidence proves operation.
- Repository changes affecting the ETGF metamodel require controlled review and approval.

## Enterprise Taxonomy

### Governance Objects

Policy, Standard, Procedure, Requirement, Control, Evidence, Risk, Exception, Decision, Finding, and Remediation.

### Business Objects

Business Capability, Business Function, Value Stream, Business Process, Business Service, and Product.

### Application and Service Objects

Business Application, Application Service, Technical Service, Service Offering, API, and Integration.

### Data Objects

Data Domain, Information Object, Data Product, Authoritative Source, Data Flow, and Data Classification.

### Technology Objects

Platform, Technology Product, Technology Service, Cloud Service, Infrastructure Component, and Configuration Item.

### Architecture Objects

Principle, Reference Architecture, Pattern, Architecture Decision Record, Roadmap, and Transition State.

### Third-Party Objects

Vendor, Contract, Third-Party Service, Dependency, and Exit Plan.

## Repository Object Specifications

Each governed object shall define its purpose, authoritative definition, required metadata, owner, steward, lifecycle, approval authority, relationships, quality rules, evidence expectations, and system-of-record mapping.

Minimum requirements:

1. Identifiers shall be stable, unique, and never reused.
2. Owners and stewards are mandatory for active governed objects.
3. Lifecycle status and effective dates are mandatory where an object can be approved, superseded, restricted, sunset, or retired.
4. Critical objects shall identify business criticality, regulatory relevance, and service dependency.
5. Object records shall link to supporting evidence rather than embedding uncontrolled copies.

## Relationship Model

- Policy governs Standard.
- Standard implements Policy and constrains Technology, Application, Service, Pattern, and Delivery Work.
- Procedure executes Standard and produces Evidence.
- Requirement derives from Policy, Standard, regulation, risk, or architecture decision.
- Control satisfies Requirement and produces Evidence.
- Business Capability is enabled by Business Service and supported by Business Application.
- Business Application realizes Application Service, which depends on Technical Service and Configuration Item.
- Technology Product enables Platform, Technical Service, Application Service, or Configuration Item.
- Risk affects governed objects; Exception temporarily authorizes a deviation and requires remediation.
- Architecture Decision selects or constrains Pattern, Reference Architecture, Technology, Service, or Roadmap.

## Metadata Standard

Mandatory metadata includes object ID, name, description, owner, steward, status, version, effective date, review date, source system, classification, criticality, domain, and evidence link where applicable.

Controlled vocabularies shall be used for lifecycle state, criticality, regulatory relevance, data classification, architecture domain, and relationship type. Duplicate, orphaned, stale, and contradictory records shall be managed as data-quality defects.

## Architecture Repository Standards

- Architecture Decision Records shall capture context, options, decision, rationale, risks, conditions, and affected objects.
- Reference architectures and patterns shall identify applicability, mandatory controls, approved technologies, prohibited variations, and lifecycle state.
- Capability, application, service, integration, data, platform, and technology catalogs shall use the common taxonomy and relationship model.
- Architecture artifacts shall be reusable, version controlled, and mapped to implementation and evidence records.

## Tool and System Mapping

| Platform | Repository Role |
|---|---|
| ServiceNow Enterprise Architecture / APM | Architecture portfolio, business applications, capabilities, roadmaps, and architecture records |
| ServiceNow CSDM / CMDB | Business applications, application services, technical services, service offerings, configuration items, and dependencies |
| ServiceNow IRM and Archer | Requirements, controls, risks, exceptions, findings, attestations, and evidence references |
| ADO and Jira | Epics, features, stories, remediation actions, acceptance criteria, and delivery evidence |
| GitHub | Version-controlled policy, standards, procedures, architecture-as-code, decisions, templates, and release manifests |
| SharePoint / M365 | Controlled publication and collaboration where designated by records management |
| Power BI | Executive dashboards and governed reporting sourced from authoritative systems |

## Repository Quality Controls

- Completeness: required fields and mandatory relationships are populated.
- Correctness: values agree with authoritative source systems and approved decisions.
- Consistency: taxonomy, lifecycle states, names, and relationships are used uniformly.
- Timeliness: records are reviewed and updated within established cadence.
- Uniqueness: duplicate active records are prevented or reconciled.
- Integrity: orphaned objects and broken relationships are detected and remediated.
- Traceability: policy-to-requirement-to-control-to-evidence and capability-to-service-to-technology relationships are demonstrable.

## Metrics and Reporting

- Application, capability, service, technology, and control coverage rates.
- Ownership and stewardship completeness.
- Relationship density and orphan rate.
- Stale artifact and overdue review rate.
- Lifecycle accuracy and unsupported technology exposure.
- Reference architecture and pattern reuse.
- Architecture decision closure and conditional approval aging.
- Evidence completeness and unproven control count.

## Implementation and Migration

1. Inventory current repositories and designate authoritative systems by object type.
2. Normalize identifiers, taxonomy, lifecycle values, ownership, and metadata.
3. Migrate approved records in controlled waves starting with policy, standards, requirements, controls, capabilities, applications, services, and technologies.
4. Reconcile duplicates and broken relationships before production acceptance.
5. Implement data-quality controls, dashboards, and stewardship queues.
6. Link delivery backlog items to repository defects and migration acceptance criteria.
7. Complete executive acceptance and transition repository operations to business-as-usual governance.

## Deliverable Inventory

- Repository charter and governance model.
- Enterprise taxonomy and controlled vocabulary.
- Object specification catalog.
- Relationship model and cardinality rules.
- Metadata and naming standard.
- Tool and system-of-record mapping.
- Repository quality control catalog.
- Metrics and dashboard specification.
- Migration backlog and acceptance checklist.
- Import templates for ServiceNow, Archer/IRM, ADO/Jira, and GitHub-managed artifacts.

## Status

Bootstrap baseline published for ETGF Version 1.0 consolidation.
