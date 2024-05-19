#!/usr/bin/env python3

def conversion_to_fahrenheit(celsius):
    if 'C' in celsius:
        celsius = celsius[:-1]

    celsius = int(celsius)
    temp = (celsius * 1.8) + 32
    print(f'{celsius}C is {temp}F')


if __name__ == "__main__":
    user_c = input(f'Enter a temperature: ')
    conversion_to_fahrenheit(user_c)
