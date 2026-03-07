from datetime import datetime

kata = (2019, 9, 25, 3, 30)

def main():
    date = datetime(*kata) # year; mouth; day; hour; minute
    print(date.strftime("%m/%d/%Y %H:%M"))

if __name__ == "__main__":
    main()