#!/usr/bin/env python3

def temp_taking():
    from statistics import mean
    temp_list = []

    while True:
        temperature = input(f'Enter a temperature: ')
        if 'C' in temperature:
            temperature = temperature[:-1]
        elif temperature == '':
            break
        else:
            temperature = int(temperature)
            temp_list.append(temperature)

    if len(temp_list) > 0:
        print(temp_list)
        print(f"Highest temperature was: {max(temp_list)}C")
        print(f"Lowest temperature was: {min(temp_list)}C")
        print(f"Average temperature was: {mean(temp_list): .2f}C")
    else:
        print('No items added')


if __name__ == "__main__":
    temp_taking()
