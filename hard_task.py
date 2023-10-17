# Даны целое число k(1 <= k <= 190) и последовательность цифр 10111213...9899, в которой выписаны подряд все двузначные числа. Определить:
# номер пары цифр, в которую входит k-я цифра;
# двузначное число, образованное парой цифр, в которую входит k-я цифра;
# k-ю цифру, если известно, что: k-четное число; k-нечетное число.

k = int(input("Enter number: "))
numbers = [x for x in range(10, 100)]
print(numbers)

# номер пары цифр, в которую входит k-я цифра.
if k % 2 == 0:
    print("The number of a pair of digits:", k//2 - 1)
else:
    print("The number of a pair of digits:", k//2)

# двузначное число, образованное парой цифр, в которую входит k-я цифра
if k % 2 == 0:
    print("Two-digit number:", numbers[k//2 - 1])
else:
    print("Two-digit number:", numbers[k//2])

# k-ю цифру, если известно, что: k-четное число; k-нечетное число.
if k % 2 == 0:
    print("k-th digit:", numbers[k//2 - 1] % 10)
else:
    print("k-th digit:", numbers[k//2] // 10)
