# Известна стоимость монитора, системного блока, клавиатура и мышь.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?

monitor = 15_000
system_unit = 45_000
keyboard = 5_000
mouse = 2_500

N = int(input("Enter count PC's: "))
print("Total price:", (N * (monitor + system_unit + keyboard + mouse)))
