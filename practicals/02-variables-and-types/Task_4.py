#!/usr/bin/env python3
if __name__ == "__main__":

    student_n = int(input('How many pupils? '))
    sweet_q = int(input('How many sweets? '))

    sweets_each = sweet_q // student_n
    left_out = sweet_q % student_n
    
    if sweet_q < student_n:
        print(f'Not enough people available to make a group')
    elif left_out == 1:
        print(f'There will be', sweets_each, 'sweets for each student with', left_out, 'sweet left over\n')
    else:
        print(f'There will be', sweets_each, 'sweets for each student with', left_out, 'sweets left over\n')

