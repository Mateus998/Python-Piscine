import sys
import string


def erase_ponctuation(words: list[str]) -> list[str]:
    translation_table = str.maketrans("", "", string.punctuation)

    return [w.translate(translation_table) for w in words]

def main():
    if len(sys.argv) != 3:
        print("ERROR")
        return
    num: int = 0
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("ERROR")
        return
    
    # split in words
    words: list[str] = sys.argv[1].split()

    # erase ponctuation
    translation_table = str.maketrans("", "", string.punctuation)
    words = [w.translate(translation_table) for w in words]

    print([w for w in words if len(w) >= num])


if __name__ == "__main__":
    main()