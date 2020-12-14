################################################################################
## Demonstration program for class Date
################################################################################

local = True

if local:
    from Labs.lab11 import date
else:
    import date


def default_test():
    A = date.Date(1, 1, 2014)

    print(A)
    print(A.to_iso())
    print(A.to_mdy())
    print(A.is_valid())
    print()

    B = date.Date(12, 31, 2014)

    print(B)
    print(B.to_iso())
    print(B.to_mdy())
    print(B.is_valid())
    print()

    C = date.Date()

    C.from_iso("2014-07-04")

    print(C)
    print(C.to_iso())
    print(C.to_mdy())
    print(C.is_valid())
    print()

    D = date.Date()

    D.from_mdy("March 15, 2015")

    print(D)
    print(D.to_iso())
    print(D.to_mdy())
    print(D.is_valid())
    print()

    E = date.Date()

    print(E)
    print(E.to_iso())
    print(E.to_mdy())
    print(E.is_valid())
    print()


def custom_test():
    """
    Test a custom input and determine if the Date class can initialize
    correctly
    """
    print('=' * 30)
    print('{:^30}'.format('CUSTOM TESTING'))
    print('\n\tOptions:\n[1]: Test __init__ and from functions from '
          'whitespace\n[2]: Test from_iso\n[3]: '
          'Test '
          'from_mdy\n[q]: Return to main screen ')
    option = input('====> ')
    acceptable = ['1', '2', '3', 'q']
    while option != 'q':
        while option not in acceptable:
            print('Invalid option: ')
            option = input('====> ')
        F = date.Date()
        if option == '1':
            month, day, year = list(
                map(int, input('Enter a month, day, and year '
                               'seperated by a space\n====> '
                               '').split()))
            F = date.Date(month, day, year)
            if F.is_valid():
                print('Acceptable Month, Day, and Year!')
                print(F)
            else:
                print('Unacceptable Date')
            F.from_iso('{}-{}-{}'.format(year, month, day))
            if F.is_valid():
                print('Acceptable Month, Day, and Year!')
                print(F)
            else:
                print('Unacceptable Date')
            F.from_mdy('{} {}, {}'.format(month, day, year))
            if F.is_valid():
                print('Acceptable Month, Day, and Year!')
                print(F)
            else:
                print('Unacceptable Date')

        elif option == '2':

            F = date.Date()
            F.from_iso(input('Enter a date in the format ('
                             'yyyy-mm-dd)\n===> '))
        elif option == '3':

            F = date.Date()
            F.from_mdy(input('Enter a date in the format ('
                             'Mmmmm '
                             'dd, yyyy)\n'
                             '====> '))

        if F.is_valid():
            print('Acceptable Month, Day, and Year!')
            print(F)
        else:
            print('Unacceptable Date')
        print(
            '\n\tOptions:\n[1]: Test __init__\n[2]: Test from_iso\n[3]: Test '
            'from_mdy\n[q]: Quit')
        option = input('====> ')

    return


def main():
    options = ['1', '2', 'q']
    MENU = 'Print default tests[1] or custom tests[2] or [q] to quit for ' \
           'the file\n====> '

    option = input(MENU)
    if option not in options:
        print('Incorrect input')
        option = input(MENU)
    while option != 'q':
        if option == '1':
            default_test()
        elif option == '2':
            custom_test()
        option = input(MENU)

    print('Thank you for testing')


if __name__ == '__main__':
    main()
