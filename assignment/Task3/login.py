#!/usr/bin/env python3
from adduser import cypher
from passwd import find_username
from getpass import getpass

if __name__ == '__main__':
    username = input("Username: ")
    password = getpass(prompt="Password: ")

    file = open("etc/passwd.txt", "r")
    username_lines = file.readlines()

    user_full = username_lines[find_username(username)]
    user_full = user_full.split(":")

    stored_password = user_full[2]
    stored_password = stored_password.replace("\n", "")

    if cypher(password) == stored_password:
        print("Access granted.")
    else:
        print("Access denied.")
