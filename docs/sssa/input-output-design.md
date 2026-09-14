# SSSA Input and Output Design

SSSA receives session information from the existing authentication/session system or from controlled prototype inputs.

## Inputs

- `session_owner` – user who owns the current session.
- `authenticated_user` – currently authenticated user.
- `session_status` – `ACTIVE`, `LOGGED_OUT`, `REVOKED` or `INVALIDATED`.
- `user_switch` – whether a new authenticated user has started using the shared device.
- `previous_session_usable` – whether the previous user's session is still usable.
- `idle_minutes` – number of minutes the session has been inactive.
- `sensitive_action` – whether the user is requesting a sensitive action.
- `assurance_state` – `NORMAL` or `REDUCED`.

## Validation

If required information is missing or invalid, SSSA applies `SSSA-P01` and returns `DENY`.

## Policy Checks

- User does not match session owner → `SSSA-P02`
- Invalid session is reused → `SSSA-P03`
- User switches while previous session is usable → `SSSA-P04`
- Inactivity reaches 5 minutes → `SSSA-P05`
- Sensitive action with reduced assurance → `SSSA-P06`
- No other policy applies → `SSSA-P07`

## Outputs

SSSA returns:

- `decision` – `PASS`, `REAUTH_REQUIRED` or `DENY`
- `matched_policy` – policy that caused the decision
- `reason` – simple explanation of the decision

## Decision Priority

`DENY > REAUTH_REQUIRED > PASS`
