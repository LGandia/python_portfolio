#!/usr/bin/env python3

if __name__ == "__main__":
    password = input("Input password: ")
    password_confirmation = input("Confirm password: ")
    if password == password_confirmation:
        print(f'Password set')
    else:
        print(f'Password setting failed, passwords not equal')
