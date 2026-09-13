from cape.validator import validate_inputs
from cape.policy_engine import check_policies


def evaluate_access(resource_sensitivity, device_status, network_location):

    valid, message = validate_inputs(resource_sensitivity, device_status, network_location)
    
    if not valid:
        return "BLOCK", "CAPE-P01", message

    return check_policies(resource_sensitivity, device_status, network_location)