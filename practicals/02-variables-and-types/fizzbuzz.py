#!/usr/bin/env python3

if __name__ == "__main__":
    '''
    def fizz_buzz(n):
        fizz = False
        buzz = False
        if n % 3 == 0:
            fizz = True
        if n % 5 == 0:
            buzz = True
        if fizz is True and buzz is True:
            print(f'FizzBuzz')
        elif fizz is True and buzz is False:
            print(f'Fizz')
        elif fizz is False and buzz is True:
            print(f'Buzz')
        else:
            print(n)


    for i in range(40):
        fizz_buzz(i)
    '''

    # alternate solution
    for n in range(40):
        fizz = False
        buzz = False

        if n % 3 == 0:
            fizz = True
        if n % 5 == 0:
            buzz = True

        if fizz is True and buzz is True:
            print(f'FizzBuzz')
        elif fizz is True and buzz is False:
            print(f'Fizz')
        elif fizz is False and buzz is True:
            print(f'Buzz')
        else:
            print(n)
