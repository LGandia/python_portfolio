#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    arguments = []
    for i in range(1, len(sys.argv)):
        arguments.append(sys.argv[i])

    arguments.sort()
    print(f'Smallest argument was: {arguments[1]}')
