#!/usr/bin/env python3
def factor(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


if __name__ == "__main__":
    try:
        num = int(input("Insert a number: "))
        assert num > 1

    except ValueError:
        print("That is not a number.")
    except AssertionError:
        print("Please input a positive number.")
    else:
        print(f'The factors of {num} are: {factor(num)}')
