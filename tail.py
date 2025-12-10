import sys


def process_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error opening file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)
    return lines


def print_last(lines, count):
    start = max(0, len(lines) - count)
    for i, line in enumerate(lines[start:], start=start + 1):
        print(f"{line.rstrip()}")


def main():
    count = 10
    if len(sys.argv) == 1:
        lines = sys.stdin.readlines()
        count = 17
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        lines = process_file(filename)
    else:
        for i in range(1, len(sys.argv)):
            filename = sys.argv[i]
            lines = process_file(filename)
            print(f"==> {filename} <==")
            print_last(lines, count)
            print(f"")
        return
    print_last(lines, count)


if __name__ == "__main__":
    main()
