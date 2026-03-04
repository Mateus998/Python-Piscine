import string
import sys
from collections import Counter
from typing import Literal

def classify(c: str) -> Literal["space", "punct", "upper", "lower", "other"]:
    if c == " ":
        return "space"
    elif c in string.punctuation:
        return "punct"
    elif c.isupper():
        return "upper"
    elif c.islower():
        return "lower"
    else:
        return "other"

def text_analyser(text=None) -> None:
    """
    Takes a single string as argument and displays the sums of its upper-case, lower-case, punctuation and spaces characters.
    If None or nothing is provided, the user is prompted to provide a string.
    If the argument is not a string, print an error message.
    """
    if text is None:
        text = input("Incert a string\n")
    elif not isinstance(text, str):
        print("String argument required")
        return
    
    assert isinstance(text, str), "argument is not a string"

    counts = Counter(classify(c) for c in text) #generator expression expressao for variavel in iteravel

    # upper = sum(1 for c in text if c.isupper())
    # upper = sum(c.isupper() for c in text)

    print(f'The text contains {len(text)} character(s):')
    print(f'- {counts["upper"]} upper letter(s)')
    print(f'- {counts["lower"]} lower letter(s)')
    print(f'- {counts["punct"]} punctuation mark(s)')
    print(f'- {counts["space"]} space(s)')

def main():
    if len(sys.argv) > 2:
        print("More than one argument detected")
        return
    elif len(sys.argv) == 2:
        text_analyser(sys.argv[1])
    else:
        text_analyser()

if __name__ == "__main__":
    main()