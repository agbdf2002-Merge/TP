# ETGF Master Registers

## Purpose

This directory is the authoritative source area for structured ETGF registers and import-ready exports.

## Required Registers

- Master Document Register
- Master Requirements Register
- Master Control Register
- Regulatory Traceability Matrix
- Architecture Decision Register
- Exception and Risk Acceptance Register
- Technology Lifecycle Register
- Evidence Register
- Technology Register
- Platform Register
- Capability Register
- Service Register
- Application Register
- Vendor Register
- API Register
- Integration Register
- Data Domain Register
- Pattern Register
- Reference Architecture Register
- Repository Register

## Control Rules

1. Every record shall have a stable identifier.
2. Every record shall have an accountable owner and lifecycle status.
3. Relationships shall reference stable identifiers rather than free-text names where possible.
4. CSV, Excel, ServiceNow, and Archer exports shall be derivatives of the controlled register baseline.
5. Duplicate identifiers and orphan relationships shall block release validation.