#!/usr/bin/env python3

from statistics import mean

if __name__ == "__main__":
    temp_list = []
    for i in range(8, 20, 2):
        if i < 13:
            temperature = input(f'Enter {i} am temperature: ')
            if 'C' in temperature:
                temperature = temperature[:-1]

            temperature = int(temperature)
            temp_list.append(temperature)
        else:
            temperature = input(f'Enter {i - 12} pm temperature: ')
            if 'C' in temperature:
                temperature = temperature[:-1]

            temperature = int(temperature)
            temp_list.append(temperature)

    print(f"Highest temperature was: {max(temp_list)}C")
    print(f"Lowest temperature was: {min(temp_list)}C")
    print(f"Average temperature was: {mean(temp_list): .2f}C")
