#!/usr/bin/env python3

if __name__ == "__main__":

    runs_scored = 48426
    total_batting = 1014
    not_out = 162

    result = runs_scored / (total_batting - not_out)
    print(f'Batting average: ', result, '\n')
