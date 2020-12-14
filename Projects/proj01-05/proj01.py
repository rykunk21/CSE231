
# making a user defined function to compute everything we need all user
# defined functions have 2 blank lines in-between them as is standard for
# pep8 code


def meters(n):
    return round((n * 5.0292), 3)


def feet(n):
    m = n * 5.0292
    return round((m / .3048), 3)


def miles(n):
    m = n * 5.0292
    return round((m / 1609.34), 3)


def furlong(n):
    return round((n / 40), 3)


def walk_time(n):
    m = n * 5.0292
    mi = m / 1609.34
    miles_per_hour = mi / 3.1

    return round((miles_per_hour * 60), 3)


# just making a simple boolean loop to prevent the code from
# exiting due to a user who inputs something other than an integer
while True:
    try:
        rods = float(input('Input rods: '))
        print('You input {} rods.'.format(rods))
        print('\n' + 'Conversions')
        print('Meters:', meters(rods))
        print('Feet:', feet(rods))
        print('Miles:', miles(rods))
        print('Furlongs:', furlong(rods))
        print('Minutes to walk {} rods: {}'.format(rods, walk_time(rods)))
        break
    except ValueError as err:
        print('Try again but this time input a number...')
        continue
