#!/usr/bin/env python3

import sys
from statistics import mean

if __name__ == "__main__":
    temp_list = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                temp = int(sys.argv[i])
                temp_list.append(temp)

            except ValueError:
                print(f"Please insert valid arguments")
                break

        print(f"Highest temperature was: {max(temp_list)}C")
        print(f"Lowest temperature was: {min(temp_list)}C")
        print(f"Average temperature was: {mean(temp_list): .2f}C")

    else:
        print(f"No arguments given")
