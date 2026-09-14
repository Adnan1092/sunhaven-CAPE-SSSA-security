# SSSA Scope and Boundaries

## In Scope

SSSA will:

- Receive the session information required for a shared-device assurance check.
- Validate that the required session information is present and valid.
- Check whether the authenticated user matches the session owner.
- Check whether an invalidated session is being reused.
- Check whether a previous user's session remains usable after a user switch on a shared device.
- Check whether a shared-device session has reached five minutes of inactivity.
- Check whether reauthentication is required before a sensitive action when session assurance is reduced.
- Return a clear session assurance decision: `PASS`, `REAUTH_REQUIRED` or `DENY`.
- Return the matched SSSA policy and a reason for the decision.
- Apply a consistent decision priority when more than one policy applies.

## Out of Scope

SSSA will not:

- Authenticate users or verify passwords.
- Perform or configure MFA.
- Create, delete or disable user accounts.
- Assign or remove RBAC roles.
- Perform Joiner-Mover-Leaver operations.
- Replace the existing application session management system.
- Replace the existing application session lifetime controls.
- Perform access reviews or general security monitoring.
- Check Microsoft Entra ID configuration changes.

## Component Boundary

SSSA starts after a user has already been authenticated and a session exists.

It receives the session information needed for the assurance check, evaluates the information against the defined SSSA security policies, and returns a session assurance decision.

SSSA does not identify the person physically using the workstation. User identity must come from authenticated session information provided by the existing authentication system.
