# Regulatory Traceability Matrix

## Purpose

The Regulatory Traceability Matrix connects Technology Policy requirements, Enterprise Architecture standards, control objectives, evidence sources, and systems of record to applicable regulatory and supervisory expectations.

This artifact is the control-plane bridge between policy intent and audit evidence.

## Operating Rule

Every mandatory Technology Policy requirement shall be traceable to:

1. A Technology Policy domain.
2. A controlled requirement ID.
3. A control objective.
4. A regulatory or framework driver.
5. An accountable owner.
6. A system of record.
7. An evidence source.
8. A review cadence.

## Primary Regulatory and Framework Sources

| Source | Usage in Framework |
|---|---|
| FFIEC Architecture, Infrastructure, and Operations | Architecture, infrastructure, operational controls, resilience, technology lifecycle |
| FFIEC Management | Governance, policy, risk management, board/senior management oversight |
| OCC Heightened Standards | Large-bank governance, risk management framework, credible challenge |
| Federal Reserve Operational Resilience Guidance | Resilience, continuity, service dependency, recovery capability |
| FDIC Supervisory Expectations | Technology risk management, third-party oversight, governance discipline |
| Interagency Third-Party Risk Management Guidance | Vendor, SaaS, managed service, concentration, exit, and contractual risk |
| GLBA Safeguards Rule | Customer information protection, access controls, encryption, monitoring |
| SEC Regulation S-P | Customer information privacy and incident response obligations where applicable |
| NYDFS 23 NYCRR 500 | Cybersecurity governance, controls, incident reporting where applicable |
| NIST CSF 2.0 | Cybersecurity governance, identify, protect, detect, respond, recover |
| NIST SP 800-53 Rev. 5 | Security and privacy controls |
| NIST SSDF | Secure software development and DevSecOps |
| NIST AI RMF | AI risk governance, mapping, measuring, managing |
| CIS Controls v8.1 | Foundational cyber hygiene controls |
| COBIT | Governance objectives and management practices |
| ISO/IEC 27001 | Information security management controls |
| TOGAF | Enterprise Architecture governance, ADM, metamodel, architecture repository |
| BIAN | Banking capability and service-domain alignment |
| ServiceNow CSDM | Service, application, technical service, and CMDB relationship model |

## Traceability Model

```text
Policy Domain
  -> Requirement
    -> Standard
      -> Control Objective
        -> Evidence Source
          -> System of Record
            -> Regulatory / Framework Driver
```

## System-of-Record Mapping

| Governance Object | System of Record |
|---|---|
| Policy and standards | GitHub, SharePoint publication repository |
| Architecture decisions | ServiceNow EA/APM, GitHub ADRs |
| Applications | ServiceNow APM |
| Business capabilities | ServiceNow EA/APM, capability model repository |
| Business and technical services | ServiceNow CSDM/CMDB |
| Technology products | ServiceNow Technology Portfolio / CMDB |
| Risks, controls, issues, findings | Archer / ServiceNow IRM |
| Engineering evidence | Azure DevOps, Jira, GitHub |
| Exceptions and waivers | ServiceNow / Archer |
| Audit evidence | Archer / ServiceNow IRM / SharePoint evidence repository |

## Current Seed Scope

The initial RTM seed contains sixteen mapped requirement/control pairs. It should be expanded as the Master Requirements Register and Master Control Register mature.

Source file:

```text
registers/traceability/regulatory_traceability_matrix.csv
```

## Minimum Acceptance Criteria

A traceability record is complete when it has:

- Requirement ID
- Control ID
- Policy domain
- Regulatory driver
- Evidence source
- System of record
- Review cadence
- Control owner
- Status

## Governance Use

The RTM shall be reviewed during:

- Policy publication
- Standard creation or revision
- ARB material-change review
- Control testing
- Audit issue response
- Regulatory exam preparation
- Exception and waiver approval
- Technology lifecycle review
