##################################################
#   Computer Project #02
#   Compute and display information for a company which rents vehicles
#
#   Compute and display the amount of money charged for a specific customers
#   Rental
#
#   Logic:
#   Check if the user wants to continue
#   create a While true loop to run an iteration infinitely against anything
#   besides expected output. This will prevent the script from breaking if
#   the user enters something unexpected.
#   gather input from the user, if input is unexpected, break the current
#   iteration and repeat asking for the input (does not work for odometer
#   reading)
#   compute the data ( In a normal script, use a user defined function )
#                    ( call the function )
#   correctly display the output
#   repeat all the steps until the user wants to stop
###################################################


import math

BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"

PROMPT = '''\nWould you like to continue (Y/N)? '''

print(BANNER)

user_cont = input(PROMPT).upper()
while True:   # inserted a boolean loop to check if the user input is
    # anything besides Y or N
    if user_cont in 'YN':
        if user_cont == 'N':
            print('Thank you for your loyalty.')
            break   # breaks the boolean loop if the user wants to stop
        while user_cont == 'Y':  # runs this section until the user input is
            # not Y

            while True:
                customer_code = input('\nCustomer code (BDW): ').upper()
                if customer_code in 'BDW':
                    break
                else:
                    print('\n\t*** Invalid customer code. Try again. ***')
            days = int(input('\nNumber of days: '))
            odometer_start = int(input('Odometer reading at the start: '))
            odometer_end = int(input('Odometer reading at the end:   '))

            """ Start the computation of the input inside the user y block. 
            1. price is dependant on the  """

            WEEKS = math.ceil(days / 7)  # only using caps lock variables
            # because the coding standard requires it.

            miles = (odometer_end - odometer_start) * .1  # convert a 6
            # digit number into a odometer reading to the 10th place


            MILEAGE_PRICE = .25  # Symbolic Constant
            cost = 0
            if days <= 0:
                print('You cant rent a car for 0 or negative days')
                # check for negative or 0 days, which will break the script
                break
            elif days > 0:
                average_daily_miles = miles / days
                average_weekly_miles = miles / WEEKS

            if miles < 0:  # Count for negative number minus err
                miles = 100000 - abs(miles)  # check for rollover from 6 digits
            if customer_code == 'B':
                cost = 40.00 * days
                cost += (MILEAGE_PRICE * miles)
            elif customer_code == 'D':
                cost = 60.00 * days
                if average_daily_miles > 100:
                    cost += (MILEAGE_PRICE * (miles - (100 * days)))
            elif customer_code == 'W':
                cost = 190.00 * WEEKS

                if 900 < average_weekly_miles < 1500:
                    cost += (100 * WEEKS)
                elif average_weekly_miles >= 1500:
                    cost += (200 * WEEKS)
                    cost += (MILEAGE_PRICE * (miles - (1500 * WEEKS)))

            # this block is to format the price to two decimal places,
            # unless the price returns '00' then only displays one '0' the
            # price should be formatted to 2 decimal places unless the price
            # ends in 0.

            cost = '{:.2f}'.format(cost)
            if cost[-1] == '0':
                cost = cost[:-1]

            # print the computed data

            print('\nCustomer summary:')
            print('\tclassification code: {}'.format(customer_code))
            print('\trental period (days): {}'.format(days))
            print('\todometer reading at start: {}'.format(odometer_start))
            print('\todometer reading at end:   {}'.format(odometer_end))
            print('\tnumber of miles driven:  {:.1f}'.format(miles))
            print('\tamount due: $ {}'.format(cost))
            user_cont = input(PROMPT).upper()   # ask if the user wants to
            # continue
            if user_cont == 'N':
                break
    elif user_cont not in 'YN':
        print('\n\t*** Invalid answer. Try again ***')
        user_cont = input(PROMPT).upper()
