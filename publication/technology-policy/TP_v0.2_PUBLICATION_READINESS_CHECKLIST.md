# TP-v0.2 Publication Readiness Checklist

## Purpose

This checklist defines the minimum criteria required to move `TP-v0.2` from hardening release candidate to publication-ready governance package.

## Release Candidate

- Release: `TP-v0.2`
- Classification: Governance Review Draft
- Repository: `agbdf2002-Merge/TP`
- Primary package: Technology Policy Control Plane

## 1. Policy and Standards Completeness

| Check | Required | Status | Notes |
|---|---:|---|---|
| Technology Policy bootstrap exists | Yes | Complete | `governance/technology-policy/TECHNOLOGY_POLICY_BOOTSTRAP.md` |
| Enterprise Architecture Standard exists | Yes | Complete | `governance/standards/ENTERPRISE_ARCHITECTURE_STANDARD.md` |
| Technology Governance Standard exists | Yes | Complete | `governance/standards/TECHNOLOGY_GOVERNANCE_STANDARD.md` |
| Technology Lifecycle Standard exists | Yes | Complete | `governance/standards/TECHNOLOGY_LIFECYCLE_STANDARD.md` |
| ARB Operating Model exists | Yes | Complete | `governance/arb/ARB_OPERATING_MODEL.md` |
| Exception and Waiver Standard exists | Yes | Complete | `governance/exceptions/EXCEPTION_AND_WAIVER_STANDARD.md` |

## 2. Register Completeness

| Check | Required | Status | Notes |
|---|---:|---|---|
| Master Document Register exists | Yes | Complete | `registers/master/master_document_register.csv` |
| Expanded Requirements Register exists | Yes | Complete | `registers/master/master_requirements_register_expanded.csv` |
| Expanded Control Register exists | Yes | Complete | `registers/master/master_control_register_expanded.csv` |
| Evidence Library Register exists | Yes | Complete | `governance/evidence/evidence_library_register.csv` |
| Expanded RTM exists | Yes | Complete | `registers/traceability/regulatory_traceability_matrix_expanded.csv` |
| Exception/Waiver Register exists | Yes | Complete | `registers/governance/exception_waiver_register.csv` |

## 3. Traceability Completeness

| Check | Required | Status | Notes |
|---|---:|---|---|
| Every `ETP-RQ` maps to a `CTRL` | Yes | Complete | Validated by expanded registers |
| Every `CTRL` maps to evidence | Yes | Complete | Evidence library seeded |
| RTM maps requirements, controls, and evidence | Yes | Complete | Expanded RTM added |
| Regulatory/framework mapping exists | Yes | Complete | FFIEC, OCC, NIST, CIS, COBIT, ISO, TOGAF, BIAN, CSDM |
| Systems of record identified | Yes | Complete | GitHub, ServiceNow, Archer/IRM, ADO/Jira |

## 4. Implementation Readiness

| Check | Required | Status | Notes |
|---|---:|---|---|
| ServiceNow import templates exist | Yes | Complete | `integrations/servicenow/` |
| ServiceNow field mapping exists | Yes | Complete | `servicenow_field_mapping_catalog.csv` |
| Archer/IRM import templates exist | Yes | Complete | `integrations/archer/` |
| Archer/IRM field mapping exists | Yes | Complete | `archer_irm_field_mapping_catalog.csv` |
| ADO/Jira work item templates exist | Yes | Complete | `integrations/ado-jira/` |
| ADO/Jira workflow mapping exists | Yes | Complete | `ado_jira_workflow_mapping.md` |
| Platform import sequencing exists | Yes | Complete | `integrations/import-sequencing/platform_import_sequence.md` |
| Data quality rules exist | Yes | Complete | `integrations/data-quality/import_data_quality_rules.csv` |

## 5. Validation Readiness

| Check | Required | Status | Notes |
|---|---:|---|---|
| Validation script exists | Yes | Complete | `tools/validation/validate_governance_registers.py` |
| GitHub Actions validation workflow exists | Yes | Complete | `.github/workflows/register-validation.yml` |
| Validation workflow execution reviewed | Yes | Pending | Must be reviewed in GitHub Actions |
| Broken relationships blocked before publication | Yes | Pending | Requires validation run confirmation |

## 6. Evidence and Audit Readiness

| Check | Required | Status | Notes |
|---|---:|---|---|
| Evidence library exists | Yes | Complete | 32 seeded evidence objects |
| Audit evidence guide exists | Yes | Complete | `AUDIT_EVIDENCE_PACKAGE_GUIDE.md` |
| ADR template exists | Yes | Complete | `architecture_decision_record_template.md` |
| Architecture evidence pack template exists | Yes | Complete | `architecture_evidence_pack_template.md` |
| Monthly governance report template exists | Yes | Complete | `MONTHLY_GOVERNANCE_REPORT_TEMPLATE.md` |
| Executive dashboard spec exists | Yes | Complete | `EXECUTIVE_GOVERNANCE_DASHBOARD.md` |

## 7. Publication Decision

| Decision Area | Status |
|---|---|
| Engineering package complete | Complete |
| Governance review ready | Complete |
| Platform import test ready | Complete |
| Final publication ready | Pending |

## Final Publication Blockers

The package should not be marked final until:

1. GitHub Actions register validation passes.
2. ServiceNow import dry-run is performed or formally deferred.
3. Archer/IRM import dry-run is performed or formally deferred.
4. ADO/Jira workflow test is performed or formally deferred.
5. Approver metadata and final publication date are added outside the engineering package.

## Recommended Decision

`TP-v0.2` is ready for governance review and platform-owner validation.

It is not yet final publication until validation workflow results and import dry-run decisions are captured.
