#!/usr/bin/env python3
import random
from string import ascii_letters


def encryption(text):
    interval = random.randint(2, 20)
    encrypted_text = text[0]
    text_index = 1

    while text_index < len(text):
        for i in range(interval - 1):
            encrypted_text += random.choice(ascii_letters)

        encrypted_text += text[text_index]
        text_index += 1

    while len(encrypted_text) % interval != 0:
        encrypted_text += random.choice(ascii_letters)

    return encrypted_text, interval


def decrypt(encrypted_text, interval):
    decrypted_text = ""

    for i in range(0, len(encrypted_text), interval):
        decrypted_text += encrypted_text[i]
        print(decrypted_text)

    return decrypted_text


if __name__ == "__main__":
    to_encrypt = input("Enter the text to encrypt: ")
    encryption, space_interval = encryption(to_encrypt)
    print(f"Encrypted message: {encryption}")
    print(f"Interval used: {space_interval}")

    print(f"Decrypted message: {decrypt(encryption, space_interval)}")
