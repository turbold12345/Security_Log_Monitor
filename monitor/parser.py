import re


def parse_log(filepath):
    events = []

    pattern = re.compile(
        r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
    )

    with open(filepath, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                ip = match.group(1)
                events.append({
                    "type": "failed_login",
                    "ip": ip
                })

    return events
