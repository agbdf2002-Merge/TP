# Technology Lifecycle Standard

## Document Control

| Field | Value |
|---|---|
| Document ID | ETS-003 |
| Title | Technology Lifecycle Standard |
| Parent Policy | Enterprise Technology Policy |
| Owner | Head of Enterprise Architecture |
| Executive Owner | Chief Information Officer |
| Governing Body | Architecture Review Board |
| Status | Draft |
| Version | 0.1 |
| Review Frequency | Annual or upon material change |

## 1. Purpose

This standard defines the mandatory lifecycle governance requirements for applications, platforms, infrastructure, software products, cloud services, APIs, integrations, data platforms, AI-enabled technologies, and third-party technology services.

The purpose is to reduce technology risk, control technical debt, improve resilience, support rationalization, and ensure technology decisions remain aligned to business capability, architecture strategy, security, regulatory, and operational requirements.

## 2. Scope

This standard applies to all technology assets and architecture objects, including:

- applications;
- platforms;
- infrastructure components;
- cloud services;
- network technologies;
- security technologies;
- APIs and integrations;
- data platforms;
- AI and model-enabled technologies;
- SaaS and externally hosted services;
- third-party managed services;
- end-user and productivity technologies where material to business or control operations.

## 3. Lifecycle States

The Bank SHALL maintain approved lifecycle states for technology objects.

| Lifecycle State | Description | Required Action |
|---|---|---|
| Proposed | Technology is being evaluated. | Architecture intake and risk assessment required. |
| Approved | Technology is approved for use. | Standard ownership and controls required. |
| Strategic | Technology is preferred for target-state use. | Reuse and investment encouraged. |
| Tolerated | Technology is allowed but not preferred. | Rationalization plan required where material. |
| Contained | Technology use is restricted. | New adoption prohibited unless exception approved. |
| Sunset | Technology is planned for retirement. | Retirement roadmap and funding plan required. |
| Retired | Technology is no longer approved for production use. | Residual records retained as required. |
| Prohibited | Technology is not permitted. | Use requires executive-level exception or remediation. |

## 4. Technology Intake

New technology SHALL be submitted through an approved intake process before acquisition, implementation, or production use.

Technology intake SHALL capture:

- business sponsor;
- business capability supported;
- intended use case;
- application/platform/service relationship;
- data classification;
- integration requirements;
- identity and access requirements;
- resilience requirements;
- hosting model;
- third-party involvement;
- security review requirements;
- regulatory or compliance impact;
- total cost and support model;
- target lifecycle state;
- exit or decommissioning considerations.

## 5. Lifecycle Ownership

Each material technology object SHALL have an accountable owner.

The accountable owner SHALL ensure:

- lifecycle state is accurate;
- ownership is documented;
- support model is defined;
- risk and control mappings are maintained;
- exceptions and waivers are current;
- end-of-life and end-of-support dates are tracked;
- remediation or decommissioning plans are maintained where required.

## 6. Strategic Technology Governance

Technology designated as Strategic SHALL:

- align to target-state architecture;
- have approved reference patterns or implementation guidance;
- be supported by defined owners;
- have approved security and resilience controls;
- be represented in the architecture repository;
- be mapped to business capabilities and technology services;
- be reviewed periodically for continued fit.

## 7. Tolerated and Contained Technology

Technology designated as Tolerated or Contained SHALL be managed to reduce risk and prevent uncontrolled expansion.

The Bank SHALL prohibit net-new adoption of Contained technology unless an approved exception exists.

Tolerated and Contained technology SHALL have:

- documented business justification;
- risk assessment;
- lifecycle owner;
- remediation or rationalization plan;
- target disposition;
- review date;
- ARB visibility where material.

## 8. Sunset and Retirement

Technology designated as Sunset SHALL have a retirement plan.

Retirement plans SHALL include:

- impacted business capabilities;
- impacted applications and services;
- replacement strategy;
- migration approach;
- data retention and archival requirements;
- integration retirement impacts;
- third-party contract impacts;
- security and access removal requirements;
- operational readiness impacts;
- funding and delivery ownership;
- planned retirement date.

Technology designated as Retired SHALL be removed from production use and retained only as necessary for legal, regulatory, audit, or record-retention obligations.

## 9. End-of-Life and End-of-Support

The Bank SHALL identify, track, and remediate technology approaching end-of-life or end-of-support.

End-of-life and end-of-support exposure SHALL be reviewed at least quarterly for material technology assets.

Unremediated end-of-life or unsupported technology supporting critical business services SHALL be escalated to technology risk governance.

## 10. Buy, Build, and External Product Governance

Buy-versus-build decisions SHALL be documented for material technology capabilities.

External products SHALL be assessed for:

- architecture fit;
- business capability fit;
- security posture;
- data and privacy impact;
- integration impact;
- resilience and recoverability;
- vendor viability;
- concentration risk;
- exit strategy;
- cost transparency;
- operational support model;
- regulatory impact.

The Bank SHOULD prefer reuse of approved strategic platforms and patterns before introducing new products.

## 11. Application Portfolio Management

Applications SHALL be classified and governed using approved portfolio attributes, including:

- business capability;
- business owner;
- technology owner;
- lifecycle state;
- criticality;
- data classification;
- technology stack;
- hosting model;
- resilience tier;
- integration profile;
- vendor dependency;
- cost profile;
- risk rating;
- rationalization disposition.

Application rationalization SHALL be performed periodically and SHALL prioritize duplicate capability, unsupported technology, high-risk applications, high-cost low-value applications, and applications misaligned to target-state architecture.

## 12. CMDB, CSDM, and Asset Alignment

Technology lifecycle records SHALL align to ServiceNow EA/APM, CSDM, CMDB, and asset objects where applicable.

At minimum, material technology objects SHALL be mapped to:

- business capability;
- business application;
- application service;
- business service or technology service;
- platform or infrastructure dependency;
- lifecycle state;
- accountable owner;
- criticality;
- support group;
- control and evidence references where applicable.

## 13. Exceptions and Waivers

Lifecycle deviations SHALL require approved exceptions or waivers.

Examples include:

- use of prohibited technology;
- continued use of unsupported technology;
- net-new adoption of contained technology;
- missing accountable owner;
- missing lifecycle state;
- missing decommissioning plan;
- missing resilience classification;
- unsupported third-party dependency.

## 14. Metrics and Reporting

The Bank SHALL report lifecycle governance metrics, including:

- technology lifecycle completeness;
- strategic vs. tolerated vs. contained technology distribution;
- end-of-life exposure;
- unsupported technology count;
- sunset plan completion;
- decommissioning progress;
- duplicate capability reduction;
- technology risk remediation progress;
- lifecycle exception aging;
- CMDB/APM mapping completeness.

## 15. Regulatory and Framework Alignment

This standard supports alignment to:

- FFIEC Architecture, Infrastructure, and Operations;
- FFIEC Management;
- OCC Heightened Standards;
- Federal Reserve operational resilience expectations;
- Interagency Third-Party Risk Management Guidance;
- GLBA Safeguards;
- NIST CSF 2.0;
- NIST SP 800-53;
- CIS Controls;
- COBIT;
- ISO/IEC 27001;
- TOGAF;
- BIAN;
- ServiceNow CSDM.

## 16. Enforcement

Technology lifecycle non-compliance SHALL be remediated, exceptioned, risk accepted, or escalated. Continued operation of unsupported or prohibited technology without approval SHALL be treated as a governance violation.
