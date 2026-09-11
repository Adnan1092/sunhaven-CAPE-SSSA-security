# CAPE Input and Output Design

## 1. Purpose

CAPE needs information about an access request before it can check the security policies.

This document defines the inputs CAPE uses and the result it returns.

## 2. Inputs

CAPE uses three inputs.

### Resource Sensitivity

`resource_sensitivity`

Accepted values:

- `STANDARD`
- `SENSITIVE`

This tells CAPE whether the requested resource needs additional security checks.

### Device Status

`device_status`

Accepted values:

- `TRUSTED`
- `UNTRUSTED`

This tells CAPE the supplied status of the device.

CAPE does not check the real device itself. The value is provided to the prototype.

### Network Location

`network_location`

Accepted values:

- `TRUSTED`
- `EXTERNAL`

This tells CAPE whether the request is from a trusted or external network.

CAPE does not detect the real location. The value is provided to the prototype.

## 3. Input Validation

CAPE checks that the three inputs are present and contain accepted values.

If an input is missing or invalid, CAPE-P01 returns:

`BLOCK`

## 4. Output

CAPE returns:

- `decision`
- `matched_policy`
- `reason`

The decision can be:

- `ALLOW`
- `BLOCK`
- `REQUIRE_REAUTHENTICATION`

The matched policy shows which CAPE policy caused the decision.

The reason gives a short explanation of the decision.

Example:

```text
decision = "BLOCK"
matched_policy = "CAPE-P02"
reason = "Sensitive resource requested from an untrusted device."
