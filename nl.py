import sys


def main():
    if len(sys.argv) == 1:
        lines = sys.stdin.readlines()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error opening file '{filename}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: too many command-line arguments.", file=sys.stderr)
        print("Usage: 'python nl.py <filename>' or 'python nl.py'", file=sys.stderr)
        sys.exit(1)

    for i, line in enumerate(lines, start=1):
        print(f"{i}  {line.rstrip()}")


if __name__ == "__main__":
    main()
