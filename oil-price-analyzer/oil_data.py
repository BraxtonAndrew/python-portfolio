"""Summarize daily oil price ranges from a tick-data file.

Each line of the input looks like:
    20170212 230000;54.32;18
    <date> <time>;<price>;<volume>

For every date, the script prints the lowest price, the highest price,
and the difference between them (the daily range).

Usage:
    python oil_data.py [path/to/oildata.txt]

If no path is given, 'oildata.txt' in the current folder is used.
"""

import sys


def parse_line(line):
    """Return (date, price) from one data line, or None if it is malformed."""
    try:
        date_part, rest = line.split()
        price = float(rest.split(";")[1])
    except (ValueError, IndexError):
        return None
    return date_part, price


def summarize(path):
    """Stream the file once and return {date: (low, high)}."""
    ranges = {}
    with open(path, "r") as infile:
        for line in infile:
            parsed = parse_line(line)
            if parsed is None:
                continue
            date, price = parsed
            if date not in ranges:
                ranges[date] = (price, price)
            else:
                low, high = ranges[date]
                ranges[date] = (min(low, price), max(high, price))
    return ranges


def format_date(raw):
    """Turn 20170212 into 2017-02-12."""
    return f"{raw[:4]}-{raw[4:6]}-{raw[6:]}"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "oildata.txt"
    try:
        ranges = summarize(path)
    except FileNotFoundError:
        sys.exit(f"File not found: {path}")

    print(f"{'Date':<12}{'Low':>8}{'High':>8}{'Range':>8}")
    for date in sorted(ranges):
        low, high = ranges[date]
        print(f"{format_date(date):<12}{low:>8.2f}{high:>8.2f}{high - low:>8.2f}")


if __name__ == "__main__":
    main()
