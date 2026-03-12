import argparse

ascii_to_morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  ' ': '/',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

def main():
    """
    Program to print strings passed as argument in morse code
    If no args are passed or characters are not space or alnums an ERROR is returned
    If the char is not on the morse list ? is returned
    """
    # argparse para unir argumentos em uma string e da erro se não tiver args
    parser = argparse.ArgumentParser()
    parser.add_argument("parts", nargs="+")
    args = parser.parse_args()

    text = " ".join(args.parts)
    # verifica se todos os elementos da string sao validos
    if not all(c == " " or c.isalnum() for c in text):
        print("ERROR")
        return
    # preenche uma lista com a tradução de cada char em morse e apresenta ? se nao existir
    morse = [ascii_to_morse.get(c, '?') for c in text.upper()]

    print(" ".join(morse))

if __name__ == "__main__":
    main()
    