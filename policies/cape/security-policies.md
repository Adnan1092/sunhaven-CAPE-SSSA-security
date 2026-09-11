# CAPE — Context-Aware Access Security Policy

## 1. Purpose

The purpose of this policy is to define the security rules used by the Sunhaven Context-Aware Access Policy Engine (CAPE).

Sunhaven Care uses Role-Based Access Control (RBAC) to control normal access based on a user's role. CAPE adds an extra security check by considering the conditions around an access request.

CAPE evaluates the supplied contextual information and returns one of the following decisions:

- ALLOW
- BLOCK
- REQUIRE_REAUTHENTICATION

CAPE does not replace RBAC. Normal role-based permission is assumed to have already passed before CAPE performs its contextual access check.


## 2. Scope

This policy applies only to the CAPE prototype developed for the Sunhaven Care Workforce IAM project.

CAPE receives contextual information about an access request, checks the information against the defined CAPE security policies and returns an access decision.

The current CAPE policies consider:

- Requested resource
- Device status
- Network location

The prototype uses controlled test information. It does not directly check Microsoft Intune device compliance, configure Microsoft Entra Conditional Access or perform MFA.

CAPE is an additional contextual security component and does not replace the existing IAM controls.


## 3. Security Policy Requirements

### 3.1 Missing or Invalid Context — CAPE-P01

CAPE must check that the contextual information required to make a policy decision is present and valid.

If information required to evaluate an applicable policy is missing or invalid, CAPE must return:

**BLOCK**

This prevents CAPE from automatically allowing an access request when it does not have enough valid information to perform the required security check.

**Related requirements:**

- CAPE-REQ-02 — Context Validation
- CAPE-REQ-05 — Security Decision
- CAPE-REQ-07 — Missing or Invalid Context


### 3.2 Untrusted Device Access — CAPE-P02

CAPE must check the supplied device status when a user requests a sensitive resource.

If:

- The requested resource is SENSITIVE; and
- The device status is UNTRUSTED

CAPE must return:

**BLOCK**

This provides an additional security check when sensitive Sunhaven information is requested from a device that does not meet the defined CAPE trust condition.

For this prototype, device status is supplied to CAPE as contextual information. CAPE does not directly check Microsoft Intune or determine real device compliance.

**Related requirements:**

- CAPE-REQ-03 — Policy Evaluation
- CAPE-REQ-04 — Context-Aware Evaluation
- CAPE-REQ-05 — Security Decision
- CAPE-REQ-06 — Decision Explanation


### 3.3 External Network Access — CAPE-P03

CAPE must check the supplied network location when a user requests a sensitive resource.

If:

- The requested resource is SENSITIVE; and
- The network location is EXTERNAL

CAPE must return:

**REQUIRE_REAUTHENTICATION**

This adds another security check when sensitive Sunhaven information is requested from an external network.

CAPE only returns the REQUIRE_REAUTHENTICATION decision. It does not perform MFA or reauthenticate the user itself. Another authentication component would be responsible for carrying out the required authentication.

**Related requirements:**

- CAPE-REQ-03 — Policy Evaluation
- CAPE-REQ-04 — Context-Aware Evaluation
- CAPE-REQ-05 — Security Decision
- CAPE-REQ-06 — Decision Explanation


### 3.4 Context Requirements Satisfied — CAPE-P04

CAPE may return ALLOW when:

- Required contextual information is present and valid;
- No BLOCK policy applies; and
- No REQUIRE_REAUTHENTICATION policy applies.

The final decision is:

**ALLOW**

An ALLOW decision means that CAPE found no additional contextual restriction for the access request.

This does not mean that CAPE grants the user's normal role permission. RBAC authorization is assumed to have already passed before the request reaches CAPE.

**Related requirements:**

- CAPE-REQ-03 — Policy Evaluation
- CAPE-REQ-05 — Security Decision
- CAPE-REQ-06 — Decision Explanation


## 4. Multiple Policy Handling

More than one CAPE policy may apply to the same access request.

To produce a clear and consistent result, CAPE uses the following decision priority:

1. BLOCK
2. REQUIRE_REAUTHENTICATION
3. ALLOW

BLOCK has the highest priority.

For example, a request for a sensitive resource may come from both an UNTRUSTED device and an EXTERNAL network.

In this situation:

- CAPE-P02 returns BLOCK.
- CAPE-P03 returns REQUIRE_REAUTHENTICATION.
- The final CAPE decision is BLOCK.

This provides a consistent result when multiple policies apply to the same request.

This priority rule is a simplified rule designed for the CAPE prototype. It does not claim to reproduce the complete Microsoft Entra Conditional Access process.

**Related requirement:**

- CAPE-REQ-08 — Multiple Policy Handling


## 5. Policy Boundaries

CAPE is responsible only for evaluating defined contextual access conditions and returning a security decision.

CAPE does not:

- Create, delete or disable user accounts.
- Perform Joiner-Mover-Leaver operations.
- Assign or remove user roles.
- Replace RBAC.
- Configure or perform MFA.
- Perform manager access reviews.
- Check configuration drift.
- Perform general security monitoring.

These functions belong to other parts of the Sunhaven Care IAM project.

CAPE starts when the required access request information is provided to the engine. It ends when CAPE returns its contextual access decision and the reason for that decision.


## 6. Testing and Compliance

The CAPE security policies will be checked using controlled test scenarios and automated tests.

Testing will check that:

- Missing or invalid required context is blocked.
- An untrusted device requesting a sensitive resource is blocked.
- An external network requesting a sensitive resource requires reauthentication.
- A valid request with no additional contextual restriction can return ALLOW.
- Multiple matching policies produce the correct final decision.
- CAPE provides a reason for its decision.

Test results will be saved as evidence of the CAPE implementation.

The tests will use fictional and controlled data and will not use real resident information.


## 7. References

[Microsoft Entra Conditional Access Overview](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)

[Microsoft Entra Conditional Access Policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policies)

[Microsoft Entra Conditional Access Network Assignment](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-assignment-network)

[Australian Government ISM — Guidelines for System Access](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/ism/cyber-security-guidelines/guidelines-for-system-access)

[NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
