#!/usr/bin/env python3
import sys
from statistics import mean

if __name__ == '__main__':

    try:
        file_name = sys.argv[1]
        file = open(f"{file_name}", "r")
    except IndexError:
        print(f'Missing argument!')
    except FileNotFoundError:
        print(f'Cannot open "{sys.argv[1]}"!')
    else:
        print(f'Log file analysis\n'
              f'=================')
        lines = file.readlines()

        ours = 0
        theirs = 0
        times_spent = []

        for i in range(0, len(lines)):

            temp = lines[i].split(",")
            temp = [rm.strip('\n') for rm in temp]

            if "OURS" in temp:
                ours += 1
                time = int(temp[2]) - int(temp[1])
                times_spent.append(time)

            elif "THEIRS" in temp:
                theirs += 1

        print(f'Cat visits: {ours}')
        print(f'Other cats: {theirs}')

        hours = sum(times_spent) // 60
        minutes = sum(times_spent) % 60
        print(f'\nTotal time in house: {hours} Hours, {minutes} Minutes\n')

        print(f'Average visit length:   {mean(times_spent):.0f} minutes')
        print(f'Longest visit:          {max(times_spent)} minutes')
        print(f'Shortest visit:         {min(times_spent)} minutes')
