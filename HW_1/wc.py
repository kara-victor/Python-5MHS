import sys


def process_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except OSError as e:
        print(f"Error opening file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)
    return lines


def line_stat(lines):
    count_str = len(lines)
    count_word = sum(len(line.split()) for line in lines)
    count_bite = sum(len(line) for line in lines)
    return count_str, count_word, count_bite


def main():
    if len(sys.argv) == 1:
        lines = sys.stdin.readlines()
        count_str, count_word, count_bite = line_stat(lines)
        print(f"{count_str:>7}{count_word:>8}{count_bite:>8}")
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        lines = process_file(filename)
        count_str, count_word, count_bite = line_stat(lines)
        print(f"{count_str:>7}{count_word:>8}{count_bite:>8} {filename}")
    else:
        sum_str = 0
        sum_word = 0
        sum_bite = 0
        for i in range(1, len(sys.argv)):
            filename = sys.argv[i]
            lines = process_file(filename)
            count_str, count_word, count_bite = line_stat(lines)
            print(f"{count_str:>7}{count_word:>8}{count_bite:>8} {filename}")
            sum_str += count_str
            sum_word += count_word
            sum_bite += count_bite
        print(f"{sum_str:>7}{sum_word:>8}{sum_bite:>8} total")
        return


if __name__ == "__main__":
    main()
