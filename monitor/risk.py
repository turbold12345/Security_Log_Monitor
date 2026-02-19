def calculate_risk(failed_attempts):
    if failed_attempts < 3:
        return "LOW"
    elif failed_attempts < 7:
        return "MEDIUM"
    elif failed_attempts < 15:
        return "HIGH"
    else:
        return "CRITICAL"
