# CAPE - Scope and Boundaries

## 1. Purpose

The purpose of CAPE is to add a contextual security check to the Sunhaven Care IAM project.

The existing role-based access control (RBAC) determines what a user is normally allowed to access based on their role. CAPE will focus on additional conditions around an access request and use defined security policies to make a contextual access decision.


## 2. In Scope

CAPE will focus on the following tasks:

- receive defined information about an access request
- check that the required information is available
- evaluate the request against defined CAPE security policies
- determine which policy applies to the request
- return a clear access decision

The possible CAPE decisions will be:

- ALLOW
- BLOCK
- REQUIRE_REAUTHENTICATION

The contextual information may include details such as the user's role, worker type, device context, location or network context, and the requested resource.

The exact inputs will be defined during the CAPE requirements and design stages.


## 3. Out of Scope

CAPE will not replace the existing RBAC system.

CAPE will not be responsible for:

- creating or deleting user accounts
- disabling user accounts
- Joiner-Mover-Leaver operations
- configuring MFA
- assigning or removing user roles
- manager access reviews
- configuration drift detection
- general security event monitoring

CAPE may return REQUIRE_REAUTHENTICATION as an access decision, but it will not perform or configure the actual MFA process.

CAPE will also not claim to detect real device compliance or real user location unless a reliable source for that information is implemented.


## 4. CAPE Boundary

CAPE starts when it receives the defined information needed to evaluate an access request.

It will check this information against the defined CAPE security policies and return a decision.

The basic CAPE boundary is:

Access Request  
↓  
Context Information  
↓  
CAPE Policy Evaluation  
↓  
ALLOW / BLOCK / REQUIRE_REAUTHENTICATION

CAPE is responsible for the contextual policy evaluation and the resulting decision. Other IAM functions, such as user lifecycle management, MFA configuration and normal role management, remain outside CAPE.


## 5. Separation from Existing IAM Components

CAPE is designed to work alongside the existing Sunhaven Care IAM controls rather than replace them.

RBAC determines the normal access permissions for a user's role. CAPE adds another security decision by considering defined contextual information around the current access request.

For example, a user may have the correct role to request a resource. CAPE can then evaluate the available context against a defined policy before returning the final contextual decision.

This keeps CAPE focused on context-aware access decisions and avoids duplicating the main responsibilities of the other IAM components.


## Current Status

The CAPE problem, security risk, proposed solution, scope and boundaries have now been defined.

The next stage is to define the CAPE security requirements.
