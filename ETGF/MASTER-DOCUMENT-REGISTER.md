# ETGF v1.0 Master Document Register

## Purpose

This register identifies the authoritative ETGF publication volumes, source packages, ownership, and delivery status. It is the controlling index for ETGF Version 1.0 consolidation.

## Publication Volumes

| Volume | Title | Authoritative Content | Primary Owner | Status |
|---|---|---|---|---|
| I | Enterprise Technology Policy | ETP-001 | Enterprise Architecture | Draft baseline complete |
| II | Enterprise Standards | ETS-001, ETS-002, ETS-003 | Enterprise Architecture | Draft baseline complete |
| III | Governance Engineering | Requirements, controls, regulatory traceability, taxonomy, object and relationship models | Enterprise Architecture | Draft baseline complete |
| IV | Repository and Architecture Specification | ETGF-14, ETGF-22, ETGF-26, ETGF-27 | Enterprise Architecture | Refactored baseline published |
| V | Implementation and Operating Model | ETGF-06, ETGF-07, ETGF-09, ETGF-12, ETGF-21, ETGF-25 | Enterprise Architecture | Draft baseline complete |
| VI | Regulatory, Audit and Assurance | ETGF-08, ETGF-13, ETGF-15, ETGF-17, ETGF-18, ETGF-19, ETGF-24 | Enterprise Architecture / Technology Risk | Draft baseline complete |
| VII | Executive Appendices, Registers and Templates | ETGF-00, ETGF-05, ETGF-10, ETGF-11, ETGF-16, ETGF-20, ETGF-23 | Enterprise Architecture | Draft baseline complete |

## Core Controlled Artifacts

| Artifact | Identifier | Repository Area | Status |
|---|---|---|---|
| Enterprise Technology Policy | ETP-001 | `ETGF/01-policy/` | Pending source consolidation |
| Enterprise Architecture Standard | ETS-001 | `ETGF/02-standards/` | Pending source consolidation |
| Technology Governance Standard | ETS-002 | `ETGF/02-standards/` | Pending source consolidation |
| Technology Lifecycle Standard | ETS-003 | `ETGF/02-standards/` | Pending source consolidation |
| Enterprise Requirements Register | ERR | `ETGF/03-governance-engineering/` | Pending structured publication |
| Enterprise Control Framework | ECF | `ETGF/03-governance-engineering/` | Pending structured publication |
| Regulatory Traceability Matrix | RTM | `ETGF/03-governance-engineering/` | Pending structured publication |
| Enterprise Technology Taxonomy | ETT | `ETGF/03-governance-engineering/` | Pending structured publication |
| Enterprise Object Model | EOM | `ETGF/03-governance-engineering/` | Pending structured publication |
| Enterprise Relationship Model | ERM | `ETGF/03-governance-engineering/` | Pending structured publication |
| Enterprise Architecture Knowledge Repository Specification | ETGF-27 | `ETGF/04-repository/` | Published Markdown baseline |

## Control Rules

1. Stable identifiers shall be preserved across Markdown, Word, registers, and implementation systems.
2. Markdown is the source-controlled working baseline.
3. Word documents are publication derivatives for approval and external template migration.
4. Final approvals, named approvers, and effective dates may be completed outside this repository.
5. No publication activity may redesign the approved governance architecture.
6. Superseded artifacts shall be retained and marked as replaced rather than silently overwritten.

## Next Consolidation Actions

1. Publish ETP-001 source into Volume I.
2. Publish ETS-001 through ETS-003 source into Volume II.
3. Publish structured governance engineering registers into Volume III.
4. Complete Volume IV object and relationship specifications.
5. Consolidate implementation, assurance, and executive materials into Volumes V through VII.
6. Generate Word-ready publication derivatives and a controlled ETGF v1.0 release package.
