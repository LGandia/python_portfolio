#!/usr/bin/env python3

def conversion_to_fahrenheit(celsius):
    temp = (celsius * 1.8) + 32
    print(f'{celsius}C is {temp}F')


def conversion_to_celsius(fahrenheit):
    temp = (fahrenheit - 32) / 1.8
    print(f'{fahrenheit}F is {temp: .1f}C')


if __name__ == "__main__":
    try:
        current_c = int(input('Enter celsius temperature to turn into fahrenheit: '))
        current_f = int(input('Enter fahrenheit temperature to turn into celsius: '))
        conversion_to_fahrenheit(current_c)
        conversion_to_celsius(current_f)
    except ValueError:
        print("Wrong data inputted, please enter an integer or a float value")
