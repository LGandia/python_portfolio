#!/usr/bin/env python3

def within_range(number):
    if 100 > number > 0:
        in_range = True
        print(in_range, ',number in range')
    else:
        in_range = False
        print(in_range, ',number not in range')


if __name__ == "__main__":
    user_num = int(input("Insert number: "))
    print(f'The number {user_num} is {within_range(user_num)}')
