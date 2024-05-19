#!/usr/bin/env python3
def username_exists(req_username):
    username_exist = False
    temp_list = []
    password_file = open("etc/passwd.txt", "r")
    file_lines = password_file.readlines()

    for line in file_lines:
        temp_user = line.split(":")
        temp_list.append(temp_user[0])

    if req_username in temp_list:
        username_exist = True
    return username_exist


def cypher(passwd):
    encrypted = passwd.replace(" ", "_")
    return encrypted[::-1]


if __name__ == '__main__':

    username = input('Enter new username: ')

    if username_exists(username) is False:
        real_user = input('Enter real name: ')
        password = input('Enter password: ')

        entry = username + ":" + real_user + ":" + cypher(password) + "\n"

        file = open("etc/passwd.txt", "a")
        file.write(f"{entry}")
        print("USER CREATED")
        file.close()
    else:
        print("Username already exists")
