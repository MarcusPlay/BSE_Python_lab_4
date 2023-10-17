# /usr/bin/env python3

def main(args: list):
    answer = (int(args[0]) + int(args[1])) / (int(args[2]) + int(args[3]))
    print(f"({args[0]} + {args[1]}) / ({args[2]} + {args[3]}) = {answer: .2f}")


if __name__ == "__main__":
    inp = input("Enter 4 numbers: ")
    args = inp.split(' ')
    main(args)
