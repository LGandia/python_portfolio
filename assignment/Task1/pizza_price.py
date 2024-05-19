#!/usr/bin/env python3

if __name__ == '__main__':

    print('BPP PIZZA CALCULATOR'
          '\n====================')

    PIZZA_PRICE = 12
    VALID_INPUT = ['yes', 'no', 'y', 'n']
    total_price = 0
    pizza_quantity = input('How many pizzas have been ordered? ')

    while True:
        try:
            pizza_quantity = int(input('How many pizzas have been ordered? '))
            assert pizza_quantity > 0

        except AssertionError:
            print('Enter a positive number!')
        except ValueError:
            print('Enter a valid number, that is text!!')

        else:
            total_price = pizza_quantity * PIZZA_PRICE
            break

    is_delivery = input('Delivery required? ')
    is_delivery = is_delivery.lower()

    if is_delivery not in VALID_INPUT:
        while is_delivery not in VALID_INPUT:
            print('Please answer with Y (yes) or N (no): ')
            is_delivery = input('Delivery required? ')
            is_delivery = is_delivery.lower()
    else:
        if pizza_quantity < 5 and is_delivery == 'y' or is_delivery == 'yes':
            total_price = total_price + 2.50

        is_tuesday = input('Is it Tuesday? ')
        is_tuesday = is_tuesday.lower()

        if is_tuesday not in VALID_INPUT:
            while is_tuesday not in VALID_INPUT:
                print('Please answer with Y (yes) or N (no): ')
                is_tuesday = input('Is it Tuesday? ')
                is_tuesday = is_tuesday.lower()
        else:
            if is_tuesday == 'y' or is_tuesday == 'yes':
                total_price = total_price/2

        is_app_order = input('Has it been delivered through the app? ')
        is_app_order = is_app_order.lower()

        if is_app_order not in VALID_INPUT:
            while is_app_order not in VALID_INPUT:
                print('Please answer with Y (yes) or N (no): ')
                is_app_order = input('Has it been delivered through the app? ')
                is_app_order = is_app_order.lower()
        else:
            if is_app_order == 'y' or is_app_order == 'yes':
                total_price = total_price * 3 / 4

    print(f'£{total_price: .2f}')

