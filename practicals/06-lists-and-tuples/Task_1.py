#!/usr/bin/env python3

if __name__ == "__main__":
    try:
        num = int(input("Insert a positive number: "))
        assert num > 1

    except AssertionError:
        print("That is a negative number")
    except ValueError:
        print("That is not a number.")
    else:
        binary = bin(num)
        binary = binary.replace('b', '')
        print(f"{binary}")

