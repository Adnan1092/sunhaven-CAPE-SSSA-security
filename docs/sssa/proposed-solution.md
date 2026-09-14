# SSSA Proposed Solution

To address the session security risks of shared workstations, the Sunhaven Shared-Device Session Assurance (SSSA) component is proposed.

SSSA will act as an additional security check for authenticated sessions used on shared devices. It will evaluate session information to determine whether the session is still safe to continue.

SSSA will check conditions such as whether the session is valid, whether the authenticated user matches the session owner, whether an old session is being reused, whether a previous user's session remains active after a user switch, and whether the shared device has been inactive for the defined period.

When additional identity assurance is needed, such as after five minutes of inactivity or before a sensitive action under reduced session assurance, SSSA will require reauthentication.

Based on these checks, SSSA will return one of three decisions:

- `PASS` – the session can continue.
- `REAUTH_REQUIRED` – the user's identity must be confirmed again before continuing.
- `DENY` – the session must not continue.

SSSA does not perform authentication, MFA, RBAC, user provisioning or Joiner-Mover-Leaver operations. It provides an additional session assurance decision for the existing Sunhaven Care IAM system.
