#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    values = len(sys.argv)
    numbers = []
    for x in range(1, values):
        numbers.append(sys.argv[x])

    min_num = min(numbers)
    print(f'Shortest argument {min_num}')
