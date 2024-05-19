#!/usr/bin/env python3

if __name__ == "__main__":
    password = input("Input password (must be between 8-12 characters): ")
    if len(password) < 8:
        print(f'Password too short')
    elif len(password) > 12:
        print(f'Password too long')
    else:
        password_confirmation = input("Confirm password: ")
        if password == password_confirmation:
            print(f'Password set')
        else:
            print(f'Password setting failed, passwords not equal')
