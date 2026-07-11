# Enterprise Architecture Standard

## Document Control

| Field | Value |
|---|---|
| Document ID | ETS-001 |
| Title | Enterprise Architecture Standard |
| Parent Policy | Enterprise Technology Policy |
| Owner | Head of Enterprise Architecture |
| Executive Owner | Chief Information Officer |
| Governing Body | Architecture Review Board |
| Status | Draft |
| Version | 0.1 |
| Review Frequency | Annual or upon material change |

## 1. Purpose

This standard defines the mandatory architecture practices, artifacts, decision rights, review gates, and evidence expectations required to implement the Enterprise Technology Policy.

The purpose is to ensure that technology change is business-aligned, risk-informed, secure-by-design, resilient, reusable, supportable, and traceable to approved enterprise principles, standards, requirements, controls, and regulatory obligations.

## 2. Scope

This standard applies to all material technology change, including:

- new applications, platforms, products, and technology services;
- material changes to existing applications, platforms, products, and technology services;
- cloud, infrastructure, network, security, data, API, integration, and AI-enabled architecture changes;
- externally hosted, SaaS, managed service, or third-party technology solutions;
- decommissioning, rationalization, and lifecycle disposition decisions;
- architecture exceptions and waivers.

## 3. Normative Language

The terms SHALL, MUST, SHOULD, MAY, and MUST NOT are used in accordance with RFC 2119 intent.

## 4. Architecture Operating Capabilities

The Bank SHALL maintain the following Enterprise Architecture operating capabilities:

| Capability | Required Outcome |
|---|---|
| Architecture Strategy | Technology direction, principles, target-state roadmaps, and business-aligned investment guidance are maintained. |
| Architecture Frameworks | Common taxonomy, metamodel, patterns, and architecture methods are maintained. |
| Architecture Community and Workforce | Architecture skills, role clarity, community practice, and reusable knowledge are maintained. |
| Architecture Innovation | Emerging technology and AI experimentation are governed and aligned to strategy. |
| Architecture Delivery Enablement | Design-time guidance, reference architectures, CI/CD guardrails, and tollgates are maintained. |
| Architecture Governance and Risk Oversight | ARB, decisions, standards, compliance, exceptions, and waivers are governed. |
| Architecture Operations Configuration and Asset Alignment | Architecture intent is aligned to ServiceNow EA/APM, CSDM, CMDB, asset, and service models. |

## 5. Architecture Governance Requirements

### 5.1 ARB Review

The Bank SHALL require Architecture Review Board review for material technology change before implementation.

ARB review SHALL evaluate:

- business capability alignment;
- target-state architecture alignment;
- security and privacy impact;
- resilience and recovery impact;
- integration and API impact;
- data classification and data movement;
- third-party and concentration risk;
- technology lifecycle risk;
- operational supportability;
- regulatory and control impact;
- exception or waiver requirements.

### 5.2 Decision Authority

ARB SHALL be the decision authority for architecture alignment, architecture conditions, architecture exceptions, and architecture waivers unless delegated in writing through the approved governance model.

### 5.3 Evidence Required

Architecture decisions SHALL be supported by evidence sufficient for audit, risk review, and operational execution.

Minimum evidence includes:

- architecture decision record;
- current-state and target-state architecture views;
- business capability mapping;
- application/platform/service ownership;
- security and risk assessment;
- resilience and recovery assessment;
- data classification and privacy impact;
- integration/API assessment;
- third-party assessment, where applicable;
- exception or waiver record, where applicable.

## 6. Architecture Repository Requirements

The Bank SHALL maintain an authoritative architecture repository. The repository SHALL include, at minimum:

- business capabilities;
- business services;
- technology services;
- applications;
- platforms;
- APIs and integrations;
- data domains;
- technology products;
- reference architectures;
- architecture patterns;
- architecture decision records;
- exceptions and waivers;
- lifecycle states;
- control and evidence mappings.

ServiceNow EA/APM, CSDM, CMDB, and approved source-control repositories SHOULD be used as the primary implementation mechanisms.

## 7. Architecture Principles

The Bank SHALL maintain architecture principles organized by:

| Level | Description |
|---|---|
| Level 1 | Architecture category |
| Level 2 | Principle |
| Level 3 | Solution pattern |
| Level 4 | Practice or implementation guidance |

Minimum principle domains SHALL include:

- data sharing and integration;
- flexible architecture;
- quality assurance;
- application development;
- architecture governance;
- external product governance;
- buy-versus-build governance;
- security and privacy;
- resilience and recoverability;
- cloud and infrastructure;
- API and integration;
- AI and emerging technology.

## 8. Required Architecture Artifacts

Material technology change SHALL produce architecture artifacts appropriate to the risk and complexity of the change.

| Artifact | Required When | System of Record |
|---|---|---|
| Architecture Decision Record | Material technology decision | GitHub / ServiceNow EA |
| Architecture Evidence Pack | ARB-reviewed change | ServiceNow / Archer |
| Business Capability Map | Business-impacting change | ServiceNow EA/APM |
| Application/Platform Profile | Application or platform change | ServiceNow APM/CMDB |
| Security Architecture Review | Security-impacting change | Archer / ServiceNow IRM |
| Data Classification Review | Data handling or data movement | Data catalog / ServiceNow |
| API/Integration Review | API, event, data flow, or integration change | API catalog / ServiceNow |
| Resilience Assessment | Critical or important service impact | ServiceNow / IRM |
| Third-Party Assessment | Vendor/SaaS/managed service | Archer / ServiceNow IRM |
| Exception/Waiver Record | Any deviation from standard | Exception Register |

## 9. Architecture Standards

The Bank SHALL maintain standards for the following domains:

- enterprise architecture governance;
- business capability architecture;
- application architecture;
- data architecture;
- integration and API architecture;
- cloud architecture;
- infrastructure and network architecture;
- security architecture;
- identity and access architecture;
- operational resilience architecture;
- observability architecture;
- third-party technology architecture;
- technology lifecycle architecture;
- AI and emerging technology architecture;
- ServiceNow CSDM and CMDB alignment.

## 10. Exception and Waiver Management

Any deviation from approved architecture standards SHALL be documented as an exception or waiver.

Exceptions and waivers SHALL include:

- affected requirement;
- affected control;
- affected standard;
- business justification;
- risk acceptance owner;
- compensating controls;
- expiration date;
- remediation plan;
- ARB decision;
- risk approval, where required.

Open-ended exceptions are prohibited unless explicitly approved by the designated executive risk authority.

## 11. Metrics and Reporting

Enterprise Architecture SHALL report architecture governance metrics, including:

- ARB review volume;
- ARB decision cycle time;
- standard compliance rate;
- exception and waiver volume;
- exception aging;
- architecture evidence completeness;
- application lifecycle risk;
- technology lifecycle risk;
- reuse of approved patterns;
- alignment to target-state architecture;
- critical service architecture coverage.

## 12. Regulatory and Framework Alignment

This standard supports alignment to:

- FFIEC Architecture, Infrastructure, and Operations;
- FFIEC Management;
- OCC Heightened Standards;
- Federal Reserve operational resilience expectations;
- FDIC supervisory expectations;
- Interagency Third-Party Risk Management Guidance;
- GLBA Safeguards;
- SEC Regulation S-P, where applicable;
- NYDFS 23 NYCRR 500, where applicable;
- NIST CSF 2.0;
- NIST SP 800-53;
- CIS Controls;
- COBIT;
- ISO/IEC 27001;
- TOGAF;
- BIAN;
- ServiceNow CSDM.

## 13. Enforcement

Non-compliance with this standard SHALL require remediation, exception approval, or escalation to the appropriate governance and risk authority.
