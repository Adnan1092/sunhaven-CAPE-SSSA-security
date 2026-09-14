# SSSA Security Policies

These policies define how SSSA checks session security on shared devices.

## SSSA-P01 - Missing or Invalid Information
If required session information is missing or invalid:

`DENY`

## SSSA-P02 - User Mismatch
If the authenticated user does not match the session owner:

`DENY`

## SSSA-P03 - Invalid Session Reuse
If a logged-out, revoked or invalidated session is reused:

`DENY`

## SSSA-P04 - User Switch
If a new authenticated user uses the shared device while the previous user's session is still usable:

`DENY`

## SSSA-P05 - Session Inactivity
If the shared-device session reaches 5 minutes of inactivity:

`REAUTH_REQUIRED`

## SSSA-P06 - Sensitive Action
If a sensitive action is requested while session assurance is reduced:

`REAUTH_REQUIRED`

## SSSA-P07 - Safe Session
If all required checks pass and no other policy applies:

`PASS`

## Decision Priority

If more than one policy applies, SSSA uses this priority:

`DENY > REAUTH_REQUIRED > PASS`
