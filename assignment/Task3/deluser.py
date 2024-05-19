#!/usr/bin/env python3
from adduser import username_exists
if __name__ == '__main__':

    username = input('Enter username to delete: ')

    file = open("etc/passwd.txt", "r")
    lines = file.readlines()
    temp = []

    if username_exists(username) is True:
        for line in lines:
            if username not in line.strip():
                temp.append(line)
        print("User deleted")

        file = open("etc/passwd.txt", "w")
        file.writelines(temp)
        file.close()
    else:
        print("User not found")
