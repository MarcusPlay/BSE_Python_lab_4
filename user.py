# /usr/bin/env python3

def main(name, age, place):
    print(f"This is {name}")
    print(f"It is {age}")
    print(f"(S)he live in {place}")


if __name__ == "__main__":
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    place = input("Where are you live? ")
    main(name, age, place)
