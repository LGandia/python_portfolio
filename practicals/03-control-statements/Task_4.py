#!/usr/bin/env python3

if __name__ == "__main__":
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    password = input("Input password (must be between 8-12 characters): ")

    if password in BAD_PASSWORDS:
        print(f'Password is too common')

    elif len(password) < 8:
        print(f'Password too short')
    elif len(password) > 12:
        print(f'Password too long')

    else:
        password_confirmation = input("Confirm password: ")
        if password == password_confirmation:
            print(f'Password set')
        else:
            print(f'Password setting failed, passwords not equal')
