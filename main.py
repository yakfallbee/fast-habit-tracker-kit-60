"""
Habit Tracker - Main module with error handling.
"""
import argparse
import sys
from utils import format_output, write_file, timestamp

VERSION = "0.4.0"

class AppError(Exception):
    """Application-specific error."""
    pass

def process(data):
    """Process input data with validation."""
    if not data:
        raise AppError("No input data provided")
    results = []
    errors = []
    for item in data:
        try:
            result = item.strip()
            if not result:
                errors.append(f"Empty item skipped")
                continue
            results.append(result)
        except Exception as e:
            errors.append(f"Error processing '{item}': {e}")
    return results, errors

def run(args):
    """Main entry point."""
    if args.version:
        print(f"Habit Tracker v{VERSION}")
        return

    if not args.input:
        print("No input provided. Use --help for usage.", file=sys.stderr)
        sys.exit(1)

    try:
        results, errors = process(args.input)
    except AppError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if errors:
        for err in errors:
            print(f"Warning: {err}", file=sys.stderr)

    output = format_output(results, args.format)

    if args.output:
        try:
            write_file(args.output, output)
            print(f"Output written to {args.output}")
        except IOError as e:
            print(f"Error writing to {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)

def main():
    parser = argparse.ArgumentParser(description="Habit Tracker")
    parser.add_argument("input", nargs="*", help="Input data")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-f", "--format", choices=["text", "json", "csv"], default="text")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
