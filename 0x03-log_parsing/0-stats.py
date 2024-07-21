#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def print_stats():
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def handle_line(line):
    """Processes a single line of input."""
    global total_size

    parts = line.split()
    if len(parts) < 7:
        return

    try:
        file_size = int(parts[-1])
        status_code = parts[-2]
        total_size += file_size

        if status_code in status_counts:
            status_counts[status_code] += 1
    except ValueError:
        pass

def signal_handler(sig, frame):
    """Handles the signal interruption."""
    print_stats()
    sys.exit(0)

# Set up signal handling for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        handle_line(line)
        line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

