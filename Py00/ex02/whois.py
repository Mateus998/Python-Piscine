import sys

def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        return
    elif len(sys.argv) == 1:
        return
    try:
        n = int(sys.argv[1])
        if n == 0:
            print("I'm Zero.")
        elif n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main()