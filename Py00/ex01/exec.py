import sys

def parse_input(argv: list[str]) -> str | None:
    args = argv[1:]

    if not args:
        print("Usage: python3 exec.py <string>")
        return None

    return " ".join(args)


def transform(text: str) -> str:
    return text[::-1].swapcase()


def main():
    text = parse_input(sys.argv)
    if text is None:
        return
    
    result = transform(text)
    print(result)


if __name__ == "__main__":
    main()
