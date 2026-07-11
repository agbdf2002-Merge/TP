# Import Validation Runbook

## Purpose

This runbook defines the minimum validation process before importing Technology Policy governance objects into ServiceNow, Archer / IRM, ADO, Jira, or other execution systems.

The objective is simple: GitHub remains the governed source for policy objects, while downstream systems receive only validated, traceable, and controlled records.

## Scope

This runbook applies to imports involving:

- policies
- standards
- requirements
- controls
- evidence
- regulatory traceability
- ARB decisions
- exceptions and waivers
- technology lifecycle records
- architecture objects
- application portfolio records
- CSDM / CMDB records
- delivery work items

## Import Principles

1. **No orphan records**
   - Requirements shall not exist without controls.
   - Controls shall not exist without evidence expectations.
   - Exceptions shall not exist without expiration, owner, and compensating control.

2. **No uncontrolled vocabularies**
   - Lifecycle states, statuses, criticality, frequency, and object types shall use approved values.

3. **No silent transformation**
   - Any field mapping change shall be documented before import.

4. **No system-of-record confusion**
   - GitHub governs policy source.
   - ServiceNow governs architecture, application, service, and CMDB execution objects.
   - Archer / IRM governs risk, control, findings, issues, and evidence objects.
   - ADO / Jira governs delivery work items.

5. **No import without reconciliation**
   - Record counts, key fields, and relationships shall be reconciled after load.

## Pre-Import Checklist

| Step | Validation | Owner | Required Outcome |
|---|---|---|---|
| 1 | Confirm source file approved in GitHub | Enterprise Architecture | Source file approved |
| 2 | Confirm stable object IDs | Enterprise Architecture | No duplicate IDs |
| 3 | Confirm required metadata | Enterprise Architecture | Required fields complete |
| 4 | Confirm relationship mappings | Technology Risk / EA | No orphan records |
| 5 | Confirm target field mapping | Platform Owner | Mapping approved |
| 6 | Confirm controlled vocabulary values | Platform Owner | Values accepted by target system |
| 7 | Confirm sample load strategy | Platform Owner | Pilot load plan approved |
| 8 | Confirm rollback approach | Platform Owner | Rollback plan documented |

## Import Execution Steps

1. Export approved CSV from GitHub.
2. Validate object IDs and required fields.
3. Validate relationship fields.
4. Validate target system field mapping.
5. Load a controlled sample batch.
6. Reconcile sample batch.
7. Resolve defects.
8. Load approved full batch.
9. Reconcile full batch.
10. Produce import evidence package.

## Post-Import Reconciliation

| Reconciliation Area | Validation Requirement |
|---|---|
| Record count | Source count equals target count unless documented exclusions exist |
| Object IDs | Target records preserve source object IDs |
| Owners | Owner fields are populated and valid |
| Status | Status values match approved vocabulary |
| Relationships | Requirement-control-evidence relationships are intact |
| Dates | Review dates, expiration dates, and lifecycle dates are valid |
| Evidence | Import logs and reconciliation reports are retained |

## Import Evidence Package

Each import shall retain:

- approved source file
- target field mapping file
- validation results
- sample load results
- full load results
- reconciliation report
- issue log
- exception log, if applicable
- approval record

## Failure Handling

| Failure Type | Action |
|---|---|
| Duplicate IDs | Reject import and correct source |
| Missing required fields | Reject import and correct source |
| Invalid lifecycle state | Reject import or map to approved value with documented rationale |
| Missing relationship | Reject publication or create remediation work item |
| Target system error | Halt import and open platform issue |
| Partial load | Reconcile, rollback if required, and produce issue log |

## Minimum Done Criteria

An import is complete only when:

- source file is approved
- target mapping is approved
- import completed successfully
- reconciliation is complete
- exceptions are documented
- evidence package is retained
- owners accept the imported data

## Anti-Patterns

- Loading CSVs manually without reconciliation
- Creating duplicate source IDs in downstream tools
- Allowing ServiceNow or Archer to redefine policy semantics
- Using free-text values where controlled vocabulary is required
- Treating import success as control success
- Failing to retain import evidence

## Ownership

| Role | Responsibility |
|---|---|
| Enterprise Architecture | Governance object source, taxonomy, standards, architecture relationships |
| Technology Risk | Control, risk, evidence, and regulatory traceability validation |
| ServiceNow Platform Owner | ServiceNow import execution and reconciliation |
| Archer / IRM Platform Owner | Archer / IRM import execution and reconciliation |
| Delivery Governance | ADO / Jira work item alignment |
| Internal Audit | Independent review of evidence, when required |
