from random import randint

references = [
    "Don't Panic.",
    "The answer to life, the universe, and everything is 42.",
    "Bring a towel — it's more useful than you think.",
    "Space is big. Really big. You just won't believe how vastly, hugely, mind-bogglingly big it is.",
    "The ships hung in the sky in much the same way that bricks don't.",
    "The problem with being punctual is that nobody's there to see it.",
    "I love deadlines. I like the whooshing sound they make as they fly by.",
    "The most beautiful thing in the universe is improbability working properly.",
    "When in doubt, blame the Vogons.",
    "Some people think you're crazy; others just haven't had enough time to notice yet.",
]

def validate_guess(num: int, value: int) -> bool:
    if value == 42:
        print(references[randint(0, 9)])
    if num == value:
        return True
    elif num > value:
        print("Too high!")
    elif num < value:
        print("Too low!")
    return False


def win_msg(value: int, n_guess: int) -> None:
    if n_guess == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!")
        print(f"You won in {n_guess} attempts!")


def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")

    value = randint(1, 99)
    try:
        guess = input("What's your guess between 1 and 99?\n")
        n_guess = 1
        while guess != 'exit':
            num = 0
            try:
                num = int(guess)

                if num < 1 or num > 99:
                    print("That's not on the range (1 - 99)")
                elif validate_guess(num, value):
                    win_msg(value, n_guess)
                    return
                
            except ValueError:
                print("That's not a number.")

            guess = input("What's your guess between 1 and 99?\n")
            n_guess += 1
    except (KeyboardInterrupt, EOFError):
        pass
    print("Goodbye!")


if __name__ == "__main__":
    main()