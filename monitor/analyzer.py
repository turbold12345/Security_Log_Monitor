from collections import defaultdict
from .risk import calculate_risk


def analyze_events(events):
    ip_activity = defaultdict(int)

    for event in events:
        if event["type"] == "failed_login":
            ip_activity[event["ip"]] += 1

    results = []

    for ip, count in ip_activity.items():
        risk_score = calculate_risk(count)

        results.append({
            "ip": ip,
            "failed_attempts": count,
            "risk_score": risk_score
        })

    return results
