#!/usr/bin/env python3
if __name__ == "__main__":

    student_s = int(input('How many students? '))
    group_s = int(input('Required group size? '))

    group_quantity = student_s // group_s
    left_out = student_s % group_s
    
    if student_s < group_s:
        print(f'Not enough people available to make a group')
    elif left_out == 1:
        print(f'There will be', group_quantity, 'groups with ', left_out, 'student left over\n')
    else:
        print(f'There will be', group_quantity, 'groups with ', left_out, 'students left over\n')
        
