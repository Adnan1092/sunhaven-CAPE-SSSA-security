# CAPE Detailed Component Design

## Purpose

This design shows how CAPE processes an access request before returning a contextual security decision.

The detailed component diagram is available in:

`diagrams/cape/cape-detailed-component-design.png`

## Processing Flow

CAPE assumes that normal RBAC authorisation has already passed.

The component then:

1. Receives `resource_sensitivity`, `device_status` and `network_location`.
2. Validates the supplied inputs.
3. Applies CAPE-P01 if required information is missing or invalid.
4. Evaluates CAPE-P02, CAPE-P03 and CAPE-P04 for valid requests.
5. Applies the decision priority:
   `BLOCK > REQUIRE_REAUTHENTICATION > ALLOW`
6. Returns the final `decision`, `matched_policy` and `reason`.

## Implementation

The design will be implemented using simple Python.

Input validation and policy checking will use basic functions and conditions. The implementation will follow the security policies defined in:

`policies/cape/security-policies.md`

The implementation will then be tested using controlled access-request scenarios.
