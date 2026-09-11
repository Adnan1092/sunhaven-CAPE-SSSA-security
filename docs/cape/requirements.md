# CAPE - Security Requirements

## 1. Purpose

This document defines the main security requirements for the Sunhaven Context-Aware Access Policy Engine (CAPE).

These requirements describe what CAPE needs to do when checking an access request. The actual security rules and conditions will be defined separately in the CAPE security policies.


## 2. Security Requirements

### CAPE-REQ-01 - Context Input

CAPE must accept the contextual information needed to check an access request.

The exact information used by CAPE will be decided during the input and detailed design stages.


### CAPE-REQ-02 - Context Validation

CAPE must check that the required information is present and contains valid values before making a decision.

This prevents CAPE from making a decision using incomplete or invalid information.


### CAPE-REQ-03 - Policy Evaluation

CAPE must check the supplied access information against the defined CAPE security policies.

The decision must be based on these defined policies.


### CAPE-REQ-04 - Context-Aware Evaluation

CAPE must consider contextual conditions in addition to normal role-based permissions.

These conditions may include the user's role, worker type, device context, location or network context, and the requested resource.

The exact contextual information used by CAPE will be finalised during the design stage.


### CAPE-REQ-05 - Security Decision

CAPE must return one clear decision after checking an access request.

The possible decisions are:

- ALLOW
- BLOCK
- REQUIRE_REAUTHENTICATION


### CAPE-REQ-06 - Decision Explanation

CAPE must provide a reason for the decision it returns.

When a security policy affects the decision, CAPE should also identify which policy was matched.

This will make it easier to understand, test and demonstrate why a request was allowed, blocked or required reauthentication.


### CAPE-REQ-07 - Missing or Invalid Context

CAPE must safely handle required information that is missing or invalid.

If information needed by a security policy is missing or invalid, CAPE must not automatically allow the request.

The exact decision for these situations will be defined in the CAPE security policies.


### CAPE-REQ-08 - Multiple Policy Handling

CAPE must use a clear and consistent method when more than one security policy applies to the same access request.

The method for handling multiple matching policies will be defined during the security policy and detailed design stages.


## 3. Requirement Boundaries

These requirements only apply to CAPE.

CAPE does not replace the existing RBAC system. It is also not responsible for creating or disabling users, Joiner-Mover-Leaver operations, MFA configuration, role assignment, manager access reviews, configuration drift detection or general security event monitoring.

CAPE is focused on checking defined contextual information against security policies and returning a contextual access decision.


## 4. Requirements Summary

| ID | Requirement |
|---|---|
| CAPE-REQ-01 | Context Input |
| CAPE-REQ-02 | Context Validation |
| CAPE-REQ-03 | Policy Evaluation |
| CAPE-REQ-04 | Context-Aware Evaluation |
| CAPE-REQ-05 | Security Decision |
| CAPE-REQ-06 | Decision Explanation |
| CAPE-REQ-07 | Missing or Invalid Context |
| CAPE-REQ-08 | Multiple Policy Handling |


## Current Status

The eight main CAPE security requirements have been defined.

The next stage is to define the CAPE security policies used to make contextual access decisions.
