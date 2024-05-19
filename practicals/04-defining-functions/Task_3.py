#!/usr/bin/env python3
def greeter(name):

    if name == '':
        print(f'Hello, Stranger!')
    else:

        initial = name[0].upper()
        rest = name[1:].lower()

        name = initial + rest
        print(f'Hello {name}!')


if __name__ == "__main__":
    text = str(input('Enter your name: '))
    greeter(text)
