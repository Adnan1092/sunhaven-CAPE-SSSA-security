# SSSA Security Risk Analysis

Shared workstations at Sunhaven Care create additional session security risks because different staff members may use the same device during different shifts.

The main risks identified are:

1. **Unattended Session Risk**  
   A staff member may leave a shared workstation while their authenticated session is still active. Another person may then access the application using the existing session.

2. **Session Identity Mismatch Risk**  
   A session may belong to one authenticated user while a different authenticated user attempts to continue using that session. This could result in access being performed under the wrong user's identity.

3. **Old Session Reuse Risk**  
   A session that has already been logged out, revoked or invalidated may create a security risk if it can still be reused.

4. **Shared-Device User Switch Risk**  
   When one staff member finishes using a shared workstation and another authenticated staff member starts using it, the previous user's session must not remain usable.

5. **Reduced Session Assurance Risk**  
   A session may still be active even when its security assurance has been reduced, such as after the shared workstation has been left inactive. Continuing sensitive actions without confirming the user's identity could expose sensitive resident information.

These risks are important for Sunhaven Care because shared workstations may be used by permanent, casual and agency staff to access sensitive resident information.
