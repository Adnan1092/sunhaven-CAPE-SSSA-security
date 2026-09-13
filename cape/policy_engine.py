def check_policies(resource_sensitivity, device_status, network_location):
    
    if resource_sensitivity == "SENSITIVE" and device_status == "UNTRUSTED":
        return "BLOCK", "CAPE-P02", "Sensitive resource requested from an untrusted device"

    if resource_sensitivity == "SENSITIVE" and network_location == "EXTERNAL":
        return "REQUIRE_REAUTHENTICATION", "CAPE-P03", "Sensitive resource requested from an external network"

    return "ALLOW", "CAPE-P04", "No additional contextual restriction applies" 