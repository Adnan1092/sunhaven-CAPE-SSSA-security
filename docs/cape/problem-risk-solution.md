# CAPE - Problem, Security Risk and Proposed Solution

## 1. Problem Analysis

Sunhaven Care uses role-based access control (RBAC) to give users access based on their work roles, such as nurses, managers and agency workers. RBAC decides what a user is normally allowed to access based on their role.

However, checking the role alone does not consider other conditions around an access request. For example, the device or location used for the request may also be important when accessing sensitive resources.

The Sunhaven Care project also includes the idea of context-aware access using information such as the user's role, device status and location. Therefore, an additional security check is needed to consider these conditions before making the final access decision.


## 2. Security Risk Analysis

A Sunhaven Care worker may have the correct role to access a resource, but the conditions of the access request may not meet the required security rules.

For example, a nurse may normally have permission to access a sensitive resource because of the Nurse role. However, the request may come from a device or location that does not meet a defined Sunhaven security policy.

If these conditions are not checked, the access decision may depend only on the user's role. This could allow access in a situation where additional security restrictions or authentication should be required.


## 3. Proposed Solution

To address this risk, I propose to develop the Sunhaven Context-Aware Access Policy Engine (CAPE).

CAPE will provide an additional security decision alongside the existing role-based access control. It will receive defined information about an access request and compare that information with Sunhaven security policies.

Based on the policy conditions, CAPE will return one of the following decisions:

- ALLOW
- BLOCK
- REQUIRE_REAUTHENTICATION

CAPE will not replace the existing RBAC system. It will also not create or disable user accounts, perform Joiner-Mover-Leaver operations, or configure MFA.

The main purpose of CAPE is to make an additional access decision using defined contextual information instead of relying only on the user's normal role permissions.


## Current Status

The problem, security risk and proposed solution for CAPE have been identified.

The next stage is to define the scope and boundaries of CAPE before creating the detailed security requirements and policies.
