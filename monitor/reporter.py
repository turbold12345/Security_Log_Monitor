import json


def generate_report(data, output_file=None):
    summary = {
        "total_suspicious_ips": len(data),
        "details": data
    }

    print("\nSecurity Summary:")
    print(f"Suspicious IPs Detected: {len(data)}\n")

    for entry in data:
        print(f"{entry['ip']} | Attempts: {entry['failed_attempts']} | Risk: {entry['risk_score']}")

    if output_file:
        with open(output_file, "w") as f:
            json.dump(summary, f, indent=4)

        print(f"\nReport saved to {output_file}")
