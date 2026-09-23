# Business Requirements Register

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Requirements that justify control selection. SHCA CSA terms and customer BAA terms are fictional; HIPAA citations refer to 45 CFR Part 164.

| REQ | Type | Source | Requirement | Controls |
|---|---|---|---|---|
| REQ-001 | Contractual | SHCA Contract Security Addendum §2.1 | Maintain security controls aligned to the NIST SP 800-53 Rev. 5 Moderate baseline for systems that store, process, or transmit agency data. | AC-1, AC-2, AC-6, AC-18, CM-2, CM-6, CM-8, PE-3, PL-2, RA-2, SC-7, SR-2 |
| REQ-002 | Contractual | SHCA CSA §2.4 | Deliver a security assessment report and POA&M at least 90 days before go-live, then quarterly. No High POA&M item may be older than 90 days at go-live. | CA-2, CA-5, CA-7, PL-2 |
| REQ-003 | Contractual | SHCA CSA §3.2 | Enforce multi-factor authentication for all privileged access and all remote access to systems handling agency data. | AC-6(2), AC-6(5), AC-17, IA-2(1), IA-2(2) |
| REQ-004 | Contractual | SHCA CSA §3.3 | Disable access for terminated personnel within 24 hours. Recertify privileged access quarterly and all access at least annually. | AC-2, AC-2(1), AC-2(3), AC-6(7), PS-4, PS-7 |
| REQ-005 | Contractual | SHCA CSA §4.1 | Retain audit logs for systems handling agency data for at least 12 months, with at least 90 days immediately searchable. | AU-2, AU-6, AU-11 |
| REQ-006 | Contractual | SHCA CSA §5.2 | Report security incidents involving agency data to SHCA within 24 hours of discovery. Test incident response capability annually. | IR-3, IR-6, IR-8 |
| REQ-007 | Contractual | SHCA CSA §6.1 | Store, process, and access agency data only within the United States. No offshore access, including by subcontractors. | SA-9 |
| REQ-008 | Contractual | SHCA CSA §6.3 | Flow security requirements down to subcontractors handling agency data. Keep a subcontractor inventory, and obtain SHCA approval before a subcontractor accesses agency data. | PS-7, SA-9, SR-2, SR-6 |
| REQ-009 | Contractual | SHCA CSA §7.1 | Remediate vulnerabilities within: Critical 15 days, High 30 days, Moderate 90 days. | RA-5, SI-2 |
| REQ-010 | Contractual | SHCA CSA §7.4 | Use only vendor-supported software (OS, databases, runtimes) for components that process agency data, or document compensating controls approved by SHCA. | SA-22 |
| REQ-011 | Contractual | SHCA CSA §8.1 | Maintain backups of agency data. Test restoration and the contingency plan at least annually. | CP-2, CP-4, CP-9, CP-9(1) |
| REQ-012 | Regulatory | HIPAA 45 CFR 164.308(a)(1)(ii)(A)-(B) | Conduct an accurate and thorough risk analysis, and implement security measures that reduce risks to a reasonable and appropriate level. | CA-2, CA-7, PM-9, RA-2, RA-3, RA-7 |
| REQ-013 | Regulatory | HIPAA 45 CFR 164.308(a)(3)(ii)(C) | Implement procedures for terminating access to ePHI when workforce employment or engagement ends. | AC-2, AC-2(1), AC-2(3), PS-4, PS-7 |
| REQ-014 | Regulatory | HIPAA 45 CFR 164.308(a)(4)(ii)(B)-(C) | Implement policies for authorizing, establishing, documenting, reviewing, and modifying access to ePHI. | AC-1, AC-2, AC-6, AC-6(2), AC-6(5), AC-6(7), PS-3, PS-5 |
| REQ-015 | Regulatory | HIPAA 45 CFR 164.308(a)(5)(i) | Implement a security awareness and training program for all workforce members. | AT-2, AT-3 |
| REQ-016 | Regulatory | HIPAA 45 CFR 164.308(a)(6)(ii) | Identify and respond to suspected or known security incidents, mitigate harmful effects, and document incidents and outcomes. | IR-3, IR-4, IR-6, IR-8, SI-3, SI-4 |
| REQ-017 | Regulatory | HIPAA 45 CFR 164.308(a)(7)(ii)(A),(B),(D) | Maintain a data backup plan and a disaster recovery plan, with testing and revision procedures. | CP-2, CP-4, CP-9, CP-9(1) |
| REQ-018 | Regulatory | HIPAA 45 CFR 164.308(b)(1); 164.314(a) | Obtain satisfactory assurances (business associate agreements) from subcontractors that create, receive, maintain, or transmit ePHI. | CA-3, SA-9, SR-6 |
| REQ-019 | Regulatory | HIPAA 45 CFR 164.312(b) | Implement mechanisms that record and examine activity in information systems containing ePHI (audit controls). | AU-2, AU-6, AU-9, AU-11, SI-4 |
| REQ-020 | Regulatory | HIPAA 45 CFR 164.312(d) | Verify that a person or entity seeking access to ePHI is the one claimed (person or entity authentication). | IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5 |
| REQ-021 | Regulatory | HIPAA 45 CFR 164.312(a)(2)(iv), (e)(1) | Protect ePHI with encryption at rest where reasonable and appropriate, and guard against unauthorized access during transmission. | CA-3, MP-6, SC-7, SC-8, SC-12, SC-28 |
| REQ-022 | Contractual | Customer BAAs/MSAs (standard Wrenfield paper) | Notify customers of breaches of unsecured PHI within 5 business days of discovery. Answer annual security questionnaires. Allow customer audits. | IR-6 |
| REQ-023 | Commitment | SOC 2 system description commitments (CC6.1–CC6.3, CC8.1) | Restrict logical access by role, approve and remove access in a timely way, review access periodically, and authorize changes before deployment. | AC-2, AC-5, AC-6, AC-6(5), AC-6(7), CM-2, CM-3 |
| REQ-024 | Internal | Wrenfield Information Security Policy ISP-001 v4.0 and Risk Appetite Statement (Board-approved 2025-10-21) | Manage cybersecurity risk within Board-approved appetite. No Critical risk may be accepted, and High risks need CEO acceptance. | AC-1, AC-5, PM-9, RA-7 |
