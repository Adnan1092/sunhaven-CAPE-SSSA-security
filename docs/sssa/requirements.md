# SSSA Security Requirements

## SSSA-REQ-01 - Session Context Input

SSSA must receive the session information required to perform a shared-device session assurance check.

## SSSA-REQ-02 - Session Context Validation

SSSA must check that the required session information is present and valid before making a session assurance decision.

## SSSA-REQ-03 - Session Identity Check

SSSA must check whether the authenticated user matches the owner of the current session.

## SSSA-REQ-04 - Invalid Session Check

SSSA must identify when a logged-out, revoked or invalidated session is being reused.

## SSSA-REQ-05 - Shared-Device User Switch Check

SSSA must identify when a new authenticated user is using a shared device while the previous user's session remains usable.

## SSSA-REQ-06 - Inactivity Check

SSSA must check whether a shared-device session has reached the defined five-minute inactivity threshold.

## SSSA-REQ-07 - Sensitive Action Assurance Check

SSSA must check whether reauthentication is required before a sensitive action when session assurance is reduced.

## SSSA-REQ-08 - Session Assurance Decision

SSSA must return one clear decision: `PASS`, `REAUTH_REQUIRED` or `DENY`.

## SSSA-REQ-09 - Decision Explanation

SSSA must return the matched SSSA policy and a reason for the decision.

## SSSA-REQ-10 - Multiple Policy Handling

If more than one SSSA policy applies, SSSA must use the defined decision priority:

`DENY > REAUTH_REQUIRED > PASS`
