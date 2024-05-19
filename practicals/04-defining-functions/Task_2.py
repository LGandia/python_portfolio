#!/usr/bin/env python3

def case_counter(x):
    upper_c = 0
    lower_c = 0

    characters = list(x)
    print(characters)

    for i in range(len(characters)):
        if characters[i] == characters[i].lower():
            lower_c = lower_c + 1
        elif characters[i] == characters[i].upper():
            upper_c = upper_c = 1

    print(f'There are {upper_c} upper case characters '
          f'and {lower_c} lower case characters')


if __name__ == "__main__":
    case_counter('Everyone')
