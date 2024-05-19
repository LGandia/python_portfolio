#!/usr/bin/env python3

if __name__ == "__main__":

    def groups(group_size):
        group_n = group_size // 24
        left_out = group_size % 24
        if group_n < 1:
            print(f'Not enough people available to make a group')
        else:
            print(f'Total groups: ', group_n)
            print(f'People left out: ', left_out, '\n')


    groups(113)
    groups(175)
    groups(12)
