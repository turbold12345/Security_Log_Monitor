import argparse
from monitor.parser import parse_log
from monitor.analyzer import analyze_events
from monitor.reporter import generate_report
from monitor.logger import setup_logger


def get_args():
    parser = argparse.ArgumentParser(
        description="CYB Security Log Monitor"
    )
    parser.add_argument("-f", "--file", required=True,
                        help="Path to log file")
    parser.add_argument("-o", "--output",
                        help="Output JSON report file")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    setup_logger()

    events = parse_log(args.file)
    analysis = analyze_events(events)

    generate_report(analysis, args.output)
