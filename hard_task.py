# /usr/bin/env python3
# Даны целое число k(1 <= k <= 190) и последовательность цифр 10111213...9899, в которой выписаны подряд все двузначные числа. Определить:
# номер пары цифр, в которую входит k-я цифра;
# двузначное число, образованное парой цифр, в которую входит k-я цифра;
# k-ю цифру, если известно, что: k-четное число; k-нечетное число.

def find_name(k):
    numbers = [x for x in range(10, 100)]

    if k % 2 == 0:
        print("The number of a pair of digits:", k//2 - 1)
        print("Two-digit number:", numbers[k//2 - 1])
        print("k-th digit:", numbers[k//2 - 1] % 10)
    else:
        print("The number of a pair of digits:", k//2)
        print("Two-digit number:", numbers[k//2])
        print("k-th digit:", numbers[k//2] // 10)


if __name__ == "__main__":
    k = input("enter k (1 <= k <= 190): ")
    find_name(k=int(k))
