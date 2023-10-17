# /usr/bin/env python3
# Известна стоимость монитора, системного блока, клавиатура и мышь.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?

def main(N):
    monitor = 15_000
    system_unit = 45_000
    keyboard = 5_000
    mouse = 2_500
    print("Total price:", (N * (monitor + system_unit + keyboard + mouse)))


if __name__ == "__main__":
    N = int(input("Enter count of PC: "))
    main(N)
