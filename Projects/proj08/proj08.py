################################################################################
#   Computer Project 08
#
#   Design a program that can read a text file with lines of F,*M with F
#   representing the food, followed an arbitrary amount of minerals M
#
#   Functions
#   Define functions to open and read file, separate foods and minerals
#   and build a dictionary of minerals as keys with sets of foods that
#   mineral is in as the values
#
#   main():
#       open and read the file, then print the contents
#       prompt the user for what minerals they wish to display:
#       display the foods that contain all (&) or any (|) of the minerals
#       after exiting, display all the foods that contain iron for anti anemic
#       diets
#
#
################################################################################

import csv
import re  # choosing to use regular expression for multi character split


def open_file(filename=None, fp=None):
    """
    Open the file based on user input or 'FOOD.txt' if no input is provided

    :return: file pointer
    """
    if not filename:
        while True:
            try:
                filename = input("Please input a file to use: ")
                if filename == '':
                    filename = 'FOOD.txt'
                fp = open(filename, 'r')
                break
            except FileNotFoundError:
                print( "Invalid filename, please try again" )
                continue
        return fp
    else:
        fp = open( filename, 'r' )
        return fp


def read_file(fp):
    """
    Using csv.reader() read the file and pass the lines to build_dictionary

    :return: dictionary of minerals
    """
    file = csv.reader( fp )
    minerals_d = {}
    for line in file:
        build_dictionary( minerals_d, line )
    return minerals_d


def build_dictionary(D, line_list):
    """
    take a line from read_file, and build a dictionary with food as keys and
    sets of minerals for values

    :param D: the dictionary being built
    :return: nothing
    """

    # this function is inside a loop. we can continue to alter the dictionary
    # from the read_file function without returning anything

    for i, item in enumerate(line_list):
        if i == 0:  # skip the first line (food)
            continue
        else:
            # check if the key exists in the dictionary
            if item in D.keys():
                # if True: add food to current mineral.values()
                D[item].add(line_list[0])
            else:
                # if False: initialize new mineral with set containing food
                D[item] = {line_list[0]}


def food_and_minerals(D):
    """
    given the dictionary, build a list of all foods, and all minerals

    :param D: dictionary from read_file()
    :return: list(foods), list(minerals)
    """
    minerals = sorted(D.keys())
    food = []

    # the value is an iterable, so iterate over it and add to food list
    for group in D.values():
        food += [food for food in group]
    return sorted(list(set(food))), minerals


def search(minerals_str, minerals_list, D):
    """
    SEARCH FUNCTION version 2.0
        UPDATES: Reread the project description and stopped trying to do
                 multiple operations from a user command. :|

    :param minerals_str: usr; string of minerals separated by operator '&
     or '|'
    :param minerals_list: list of possible minerals to ensure usr inputs
    minerals that exist in data
    :param D: the dictionary of key values
    :return: list of foods with any (|) or all (&) minerals
    """

    # initialize a list of minerals provided by usr or STDIN
    minerals = [mineral.lower().strip() for mineral in re.split('[|&]',
                                                                minerals_str)]

    # check if a mineral is not in the mineral list and return none
    if any( mineral not in minerals_list for mineral in minerals ):
        return None

    # forget about minerals and reinitialize the values for the minerals by
    # passing them in as keys
    minerals = [D[mineral.lower().strip()] for mineral in re.split('[|&]',
                                                                minerals_str)]
    # check that exactly three minerals were passed in the str
    if len(minerals) != 3:
        return None
    else:
        # check for operator
        if '&' in minerals_str and '|' not in minerals_str:
            # do operation
            function_out = minerals[0] & minerals[1] & minerals[2]
            return function_out
        # check for operator
        elif '|' in minerals_str and '&' not in minerals_str:
            # do operation
            function_out = minerals[0] | minerals[1] | minerals[2]
            return function_out
        # illegal operator returns None
        else:
            return None


def anti_anemia(D):
    """ Returns the values from the iron key in the dictionary """
    return D['iron']


# Main function
def main():
    """
    interact with the user through the console.

    :return: nothing
    """
    PROMPT = '\n'.join(
            ['Specify three types of minerals separated by &(and) or |(or)',
             'Please enter 3 minerals using a single operand type '
             '(or q to quit): '])

    D = read_file(open_file())
    food, minerals = food_and_minerals(D)

    # print the foods, then minerals
    print("\nWe consider these foods:")
    print(*food, sep='\n')
    print("\nWe consider these minerals:")
    print(*minerals, sep='\n')
    print()

    # keep iterating until quit is desired
    option = input(PROMPT).lower()
    while option != 'q':
        lookup = search(option, minerals, D)
        if not lookup:
            print("Error in input.\n")
        else:
            print(*sorted(list(lookup)), sep='\n')

        option = input(PROMPT).lower()

    # after quit, show the values of D[iron]
    print(
        "\nFoods that contain iron, please eat these foods if you are anemic: ")
    print(*sorted(list(anti_anemia(D))), sep=', ')


# DO NOT DELETE THE NEXT TWO LINES
if __name__ == "__main__":
    main()
