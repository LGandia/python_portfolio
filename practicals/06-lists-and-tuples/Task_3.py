#!/usr/bin/env python3
def factor(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    if len(factors) == 2:
        isprime = True
    else:
        isprime = False
    return isprime


if __name__ == "__main__":
    try:
        num = int(input("Insert a number: "))
        assert num > 1

    except ValueError:
        print("That is not a number.")
    except AssertionError:
        print("Please input a positive number greater than 1.")
    else:
        if not factor(num):
            print(f'{num} is not prime')
        else:
            print(f'{num} is prime')
