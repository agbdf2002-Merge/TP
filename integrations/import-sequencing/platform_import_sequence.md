# Platform Import Sequencing

## Purpose

This runbook defines the dependency-aware load sequence for moving Technology Policy governance objects from GitHub-controlled source files into ServiceNow, Archer/IRM, and ADO/Jira.

Bad sequencing creates orphaned records, weak traceability, and governance theater. The sequence below is mandatory for pilot import validation.

---

## Source-of-Truth Rule

GitHub remains the authoritative engineering source for controlled governance objects until the appropriate platform system of record is formally activated and reconciled.

| Object Family | Authoritative Source During Bootstrap | Target System of Record |
|---|---|---|
| Policies / Standards | GitHub | ServiceNow IRM / Archer / SharePoint |
| Requirements | GitHub | Archer / ServiceNow IRM |
| Controls | GitHub | Archer / ServiceNow IRM |
| Evidence | GitHub seed, platform-generated thereafter | Archer / ServiceNow IRM / ServiceNow |
| Architecture Objects | GitHub seed | ServiceNow EA/APM |
| CSDM / CMDB Objects | GitHub seed | ServiceNow CSDM / CMDB |
| Delivery Work Items | GitHub seed | ADO / Jira |
| ARB Decisions | GitHub template | ServiceNow EA/APM / GitHub ADRs |
| Exceptions / Waivers | GitHub seed | Archer / ServiceNow IRM |

---

## ServiceNow Load Sequence

### Phase SN-01: Reference Data

1. Technology domains
2. Business capability taxonomy
3. Owner groups
4. Lifecycle states
5. Criticality values
6. Regulatory/framework reference tags

### Phase SN-02: CSDM Foundation

1. Business capabilities
2. Business services
3. Technical services
4. Service offerings
5. Service relationships

### Phase SN-03: CMDB Foundation

1. Configuration item classes
2. Configuration items
3. CI ownership
4. CI-to-service relationships
5. CI-to-application relationships

### Phase SN-04: EA / APM Objects

1. Architecture objects
2. Applications
3. Application-to-capability relationships
4. Application-to-service relationships
5. Architecture decision records
6. Approved patterns

### Phase SN-05: Governance Objects

1. Requirements
2. Controls
3. Evidence records
4. Exceptions and waivers
5. Issues and remediation actions

### ServiceNow Reconciliation Checks

- Every application maps to a business capability.
- Every technical service maps to a business service or service offering.
- Every architecture object has an owner.
- Every exception has expiration and remediation fields.
- Every ARB decision maps to a material change or architecture object.

---

## Archer / IRM Load Sequence

### Phase IRM-01: Regulatory Foundation

1. Regulatory citations
2. Framework references
3. Risk taxonomy
4. Control taxonomy
5. Evidence types

### Phase IRM-02: Governance Documents

1. Policies
2. Standards
3. Procedures, where applicable
4. Document ownership and review cadence

### Phase IRM-03: Requirements and Controls

1. Requirements
2. Requirement-to-policy mappings
3. Controls
4. Control-to-requirement mappings
5. Control testing method

### Phase IRM-04: Evidence and Risk Objects

1. Evidence objects
2. Evidence-to-control mappings
3. Risk objects
4. Risk-to-control mappings
5. Issues and findings
6. Exception and waiver records

### Archer / IRM Reconciliation Checks

- Every requirement maps to at least one policy or standard.
- Every control maps to at least one requirement.
- Every control has an owner and testing cadence.
- Every evidence record maps to a control.
- Every finding maps to remediation ownership and due date.

---

## ADO / Jira Load Sequence

### Phase WORK-01: Work Item Foundation

1. Area paths / project components
2. Teams
3. Work item types
4. Labels/tags
5. Workflow states

### Phase WORK-02: Governance Backlog

1. Architecture review epics
2. Architecture requirements
3. Control evidence tasks
4. ADR tasks
5. Exception remediation tasks
6. Lifecycle remediation tasks
7. RTM completion tasks

### Phase WORK-03: Relationship Mapping

1. Work items to requirements
2. Work items to controls
3. Work items to evidence
4. Work items to ARB decisions
5. Work items to exceptions/findings

### ADO / Jira Reconciliation Checks

- Every remediation task has a mapped requirement or control.
- Every exception remediation task has a due date.
- Every architecture review epic has an ARB decision outcome.
- Every evidence task has a target system of record.

---

## Import Package Evidence

Every platform import shall produce an evidence package containing:

1. Source file name and commit SHA
2. Import date/time
3. Import owner
4. Target system
5. Row count loaded
6. Row count rejected
7. Reconciliation results
8. Known exceptions
9. Approval to proceed or rollback decision

---

## Rollback Criteria

Rollback is required when:

- More than 5% of records fail validation.
- Parent/child references are broken.
- owner or lifecycle fields are missing from critical objects.
- duplicate IDs are created.
- evidence mappings are corrupted.

---

## Exit Criteria

Import sequencing is complete when:

- All platform imports run in dependency order.
- all reconciliation checks pass or have approved exceptions.
- row counts match approved source extracts.
- evidence package is stored in the target system of record.
- governance owner signs off on import completion.
