CYB Security Log Monitor

This project is a Python-based security log monitoring tool built to better understand how authentication logs can be analyzed to detect suspicious behavior such as repeated failed login attempts and potential brute-force activity.

The tool reads a log file, extracts failed login events, groups activity by IP address, and assigns a risk level based on the number of attempts detected. It then generates a clear summary in the terminal and can export the results as a structured JSON report.

The main goal of this project was to simulate a basic SOC-style monitoring workflow while practicing log parsing, pattern detection, risk classification, and modular software design.

Features

Authentication log parsing

Failed login detection

IP-based activity aggregation

Risk level classification (Low / Medium / High / Critical)

JSON report generation

Modular and maintainable structure
