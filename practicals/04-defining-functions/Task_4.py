#!/usr/bin/env python3

def initial_rm(word):
    if len(word) > 1:
        word = word[:-1]
        print(word)
    else:
        print(f'{word} not long enough')


if __name__ == "__main__":
    text = input('Enter a word: ')
    initial_rm(text)
