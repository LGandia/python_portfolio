#!/usr/bin/env python3
from adduser import cypher, username_exists
from getpass import getpass


def find_username(req_username):
    temp_list = []
    password_file = open("etc/passwd.txt", "r")
    file_lines = password_file.readlines()

    for x in file_lines:
        temp_user = x.split(":")
        temp_list.append(temp_user[0])
    position = temp_list.index(req_username)

    return position


if __name__ == '__main__':
    given_username = input('Enter username: ')

    if username_exists(given_username) is True:
        given_password = getpass(prompt="Current password: ")
        given_password = cypher(given_password)

        file = open("etc/passwd.txt", "r")
        username_lines = file.readlines()

        user_full = username_lines[find_username(given_username)]
        user_full = user_full.split(":")

        stored_password = user_full[2]
        stored_password = stored_password.replace("\n", "")

        new_password = getpass(prompt='New password:')
        print(new_password)
        confirm_password = getpass(prompt='Confirm password: ')
        print(confirm_password)

        if stored_password == given_password:
            if new_password == confirm_password:

                temp = []
                user_full[2] = cypher(new_password)
                user_full = ":".join(user_full)
                print(user_full)

                for line in username_lines:
                    if given_username not in line.strip():
                        temp.append(line)

                temp.append(user_full)

                file = open("etc/passwd.txt", "w")
                file.writelines(temp)
                file.close()
            else:
                print('Password confirmation failed')
        else:
            print('Sorry, wrong password')
