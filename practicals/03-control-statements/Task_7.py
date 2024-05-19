#!/usr/bin/env python3

if __name__ == "__main__":
    ttable_number = int(input("number of timetables required 0-12: "))

    if ttable_number > 12:
        print(f'Too big')
    elif ttable_number < 0:
        print(f'Too small')
    else:
        ttable_number += 1

        for i in range(0, ttable_number):
            print(i, 'x 7 =', i*7)
