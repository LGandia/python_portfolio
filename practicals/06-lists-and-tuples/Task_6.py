#!/usr/bin/env python3
def decrypt(encrypted_text, interval):
    decrypted_text = ""

    for i in range(0, len(encrypted_text), interval):
        decrypted_text += encrypted_text[i]
        print(decrypted_text)

    return decrypted_text


if __name__ == "__main__":
    try:
        encrypted = input("Input encrypted text: ")
        space_interval = int(input("Space interval used:"))
    except ValueError:
        print("Please enter valid data")
    else:
        print(f"Decrypted message: {decrypt(encrypted, space_interval)}")
