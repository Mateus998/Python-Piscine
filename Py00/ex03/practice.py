import sys
import string
from collections import Counter

def line_classify(line: str) -> str:
    level, sep, msg = line.partition(':')
    if not sep or not level or not msg:
        return "BAD_LINE"
    return level.strip()


def log_analyzer(msg=None) -> None:
    """
    Counts the occurance of each log level detected on string arg
    than counts dthe most frequent word on input
    and print all the information counted
    if None an input must be inserted
    if not string returns error
    """
    if msg is None:
        msg = input("Isert log message:\n")
    
    assert isinstance(msg, str), "String argument required"

    lines = msg.splitlines()

    levels = Counter(line_classify(l) for l in lines)
    print("Log level detected count:")
    for lvl, n in levels.items():
        print(f"{lvl}: {n}")

    for w in msg:
        if w.isspace() or w in string.punctuation:
            w = " "

    words = msg.lower().split()

    words_count = Counter(w for w in words)
    print("Top 5 most common words:")
    for w, n in words_count.most_common(5):
        print(f"{w} - {n}")


def main():
    if len(sys.argv) > 2:
        print("Too many arguments.")
        return 2
    elif len(sys.argv) == 2:
        log_analyzer(sys.argv[1])
    else:
        log_analyzer()


if __name__ == "__main__":
    main()