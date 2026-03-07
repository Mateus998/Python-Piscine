kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

def main():
    for k, v in kata.items():
        print(f"{k} was created by {v}")

if __name__ == "__main__":
    main()