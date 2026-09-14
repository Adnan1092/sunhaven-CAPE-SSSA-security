# SSSA Problem Analysis

Sunhaven Care has a high-turnover workforce that includes permanent, casual and agency staff. Staff may use shared workstations during daily work and shift changes to access sensitive resident information. After a user successfully authenticates, an application session is created for that user. However, a valid session may create a security problem if it remains available when the workstation is left unattended or is later used by another staff member.

The existing IAM system provides authentication and access controls, but shared devices require additional session assurance. A successfully authenticated session does not automatically mean that the session remains safe throughout its use. The system therefore needs a way to check whether an authenticated session is still safe to continue when session conditions change.

SSSA focuses on this problem by checking the security state of an authenticated session on a shared device. It does not replace the existing authentication, RBAC, MFA or user account management functions.
