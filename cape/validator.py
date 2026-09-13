def validate_inputs(resource_sensitivity, device_status, network_location):
    
    if not resource_sensitivity:
        return False, "Missing resource sensitivity"
    
    if not device_status:
        return False, "Missing device status"
    
    if not network_location:
        return False, "Missing network location"
    
    if resource_sensitivity not in ["STANDARD", "SENSITIVE"]:
        return False, "Invalid resource sensitivity"

    if device_status not in ["TRUSTED", "UNTRUSTED"]:
        return False, "Invalid device status"

    if network_location not in ["TRUSTED", "EXTERNAL"]:
        return False, "Invalid network location"

    return True, "Inputs are valid" 