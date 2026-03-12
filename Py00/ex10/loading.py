import time

bar_width = 40

def ft_progress(list):
    for i, l in enumerate(list, start=1):

        ratio = i / len(list)
        filled = int(ratio * bar_width)
        empty = bar_width - filled

        percent = "[" + str(ratio * 100) + "%]"
        bar = "[" + ("=" * filled) + (" " * empty) + "]"
        print(f"\r{percent} {bar}", end="")

        if ratio == 1:
            print("\n")
        yield l

for x in ft_progress(range(200)):
    time.sleep(0.01)