#!/usr/bin/env python3
def obfuscation(text):
    encrypt = text.replace(" ", "")
    return encrypt[::-1]


if __name__ == "__main__":
    to_obfuscate = input("Enter the text to obfuscate: ")
    print(obfuscation(to_obfuscate))
