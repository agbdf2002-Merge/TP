# ETGF Documentation Build Pipeline

## Purpose

Define the controlled transformation of authoritative ETGF source into Microsoft Word, PDF, SharePoint, ServiceNow Knowledge, and regulatory examination packages.

## Source-to-Publication Flow

GitHub Markdown and structured registers
→ validation and cross-reference checks
→ document assembly
→ corporate Word template
→ PDF derivative
→ publication manifest and checksums
→ SharePoint controlled publication
→ ServiceNow Knowledge distribution
→ audit and regulatory binder

## Pipeline Controls

1. Source files shall use stable identifiers.
2. Build failures shall block release packaging.
3. Broken internal links and duplicate identifiers shall fail validation.
4. Generated Word and PDF artifacts shall include version, status, and source commit metadata.
5. Publication derivatives shall not become independent editing baselines.
6. Release artifacts shall be reconciled to the release manifest.

## Validation Stages

| Stage | Validation |
|---|---|
| Source | Markdown syntax, required metadata, naming conventions |
| Identifier | Duplicate IDs, missing IDs, invalid patterns |
| Traceability | Orphan requirements, controls, evidence, and objects |
| Assembly | Volume order, headings, tables, appendices |
| Word | Table of contents, bold headings, page integrity, cross-references |
| Release | Manifest, file inventory, version, checksums, approval placeholders |

## Minimum Build Outputs

- Seven Word volumes
- Seven PDF derivatives when required
- Master register workbooks or structured exports
- Release manifest
- Release notes
- Validation report
- Artifact checksum inventory

## Publication Ownership

Enterprise Architecture owns the authoritative source and publication assembly. Risk and control partners validate control and regulatory traceability. Corporate document management owns final-template and approved-record handling.