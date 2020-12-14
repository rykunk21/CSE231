####################################################
#   Computer Project 06
#   Write a program that reads data about nuclear reactors and displays
#   information based on user input
#
#   Algorithm
#       Define functions to open a file and read its contents
#       Define functions to manipulate and return specific pieces of data
#       Define a main loop for the user to interact with
#           allow for user errors and give the user series of options
#           depending on the option, call the corresponding function and
#           display the information
####################################################

import csv
from operator import itemgetter
import matplotlib.pyplot as plt

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def open_file():
    """ Open a file given input from the user """
    while True:
        filename = input('Please input a file to use: ')
        if filename == '':  # Test for no file name input
            filename = '../../Extras/reactors-operating.csv'
        try:
            fp = open(filename, 'r',
                      encoding="windows-1252")
            break
        except FileNotFoundError:
            print('Invalid filename, please try again')
            continue
    return fp


def read_file(fp):
    """ read a file based on the file pointer  """
    next(csv.reader(fp), None)  # skip header line
    next(csv.reader(fp), None)  # skip the next header line
    return [line for line in csv.reader(fp)]


def get_reactor_location(location_string):
    """ without using regex, remove parenthesis from a location """
    function_out = ''
    typing = True   # use a bool to remove letters from a string
    for let in location_string:
        if let == '(':
            typing = False  # turn to false when parenthesis opens
            continue
        elif let == ')':
            typing = True   # turn to true when parenthesis closes
            continue
        if typing:
            function_out += let
    return '{}, {}'.format(function_out.split(',')[0].strip(),
                           function_out.split(',')[1].strip())


def reactors_per_region(master_list):
    """ Use a dictionary to store counts of reactors per region """
    master_list = sorted(master_list, key=itemgetter(5))

    values = {'NRC1': 0, 'NRC2': 0, 'NRC3': 0, 'NRC4': 0}
    NRC1_count = values['NRC1']
    NRC2_count = values['NRC2']
    NRC3_count = values['NRC3']
    NRC4_count = values['NRC4']

    for line in master_list:
        if line[5] == '1':
            NRC1_count += 1
        elif line[5] == '2':
            NRC2_count += 1
        elif line[5] == '3':
            NRC3_count += 1
        elif line[5] == '4':
            NRC4_count += 1
    return list(map(int, [NRC1_count, NRC2_count, NRC3_count, NRC4_count]))


def top_react_by_mwt(master_list):
    """ Build a list of tuples of the top 10 reactors """
    function_out = []
    local_list = []
    for line in master_list[1:]:
        local_list.append([line[-14], line[0], line[4]])
    local_list.sort(reverse=True)
    for i in range(10):
        function_out.append((int(local_list[i][0]), local_list[i][1],
                             get_reactor_location(local_list[i][2])))
    return function_out


def bot_react_by_mwt(master_list):
    """ Build a list of tuples of the bottom 10 reactors """
    function_out = []
    local_list = []
    for line in master_list:
        local_list.append([line[-14], line[0], line[4]])
    local_list.sort()
    for i in range(10):
        function_out.append((int(local_list[i][0]), local_list[i][1],
                             get_reactor_location(local_list[i][2])))
    return function_out


def reactors_in_state(master_list, state):
    """ Returns a list of all the reactors in a specific state """
    function_out = []
    for line in master_list:
        location = get_reactor_location(line[4]).split(',')[1].strip()
        if location == state:
            function_out.append((line[0], get_reactor_location(line[4])))
    return function_out


def years_active(master_list):
    """ Return a list of integers from the last column  """
    return sorted(list(map(int, [val[-1] for val in master_list])))


def plot_years_active(years_active_list):
    """
    DO NOT CHANGE
    Given list of ints, plot histogram showing age of reactors in US
    """
    plt.grid(which='both')
    plt.hist(years_active_list, bins=22, edgecolor='black')
    plt.title('Active years per Nuclear Reactor')
    plt.xlabel('Years active')
    plt.ylabel('Number of reactors')
    plt.show()


def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = 'Menu\n\
1: # Reactors in each region\n\
2: Top energy producing reactors\n\
3: Bottom energy producing reactors\n\
4: List reactors in specific state\n\
5: Plot histogram for how long reactors have been active'
    print(OPTIONS)


def main():
    """ The main loop to interact with the user """
    fp = open_file()
    master_list = read_file(fp)
    print()
    while True:     # run endlessly until the user wants to quit
        display_options()
        option = input('Choose an option, q to quit: ')
        if option == '1':   # display the reactor count by region
            print('\n{:<8}{:<8}{:<8}{:<8}'.format('NRC 1', 'NRC 2', 'NRC 3',
                                                  'NRC 4'))
            reactors = reactors_per_region(master_list)
            print('{:<8}{:<8}{:<8}{:<8}'.format(*reactors))  # * operator
            # unpacks the list so it can be accepted by the string formatting
            print()     # various empty print statements added for formatting
            continue

        elif option == '2':    # display the top 10 reactors by MWt
            print('\nTop 10 Reactors by MWt')
            print('{:<8}{:<30}{:<10}'.format('MWt', 'Reactor Name',
                                             'Location'))

            reactors = top_react_by_mwt(master_list)
            for val in reactors:
                print('{:<8}{:<30}{:<10}'.format(val[0],
                                                 val[1][:25],
                                                 val[2]))
            print()

        elif option == '3':      # display the bottom 10 reactors by MWt
            print('\nBottom 10 Reactors by MWt')
            print('{:<8}{:<30}{:<10}'.format('MWt', 'Reactor Name',
                                             'Location'))

            reactors = bot_react_by_mwt(master_list)
            for val in reactors:
                print('{:<8}{:<30}{:<10}'.format(val[0],
                                                 val[1][:25],
                                                 val[2]))
            print()

        elif option == '4':     # prints all reactors in a specific state
            abbr = input('\nPlease enter a 2 letter state code: ').upper()
            while abbr not in STATES:
                print('Please input a valid state')
                abbr = input('\nPlease enter a 2 letter state code: ').upper()
            reactors = reactors_in_state(master_list, abbr)
            if len(reactors) == 0:
                print('\nThere are 0 reactors in {}'.format(abbr))
            else:
                print('There are {} reactors in {}:'.format(len(reactors),
                                                            abbr))
            for line in reactors:
                print('{} in {}'.format(line[0], line[1]))
            print()

        elif option == '5':
            years_active_list = years_active(master_list)
            plot_years_active(years_active_list)

        elif option.lower() == 'q':
            break

        else:
            print('\nInvalid choice, please try again')
            continue


if __name__ == '__main__':
    main()
