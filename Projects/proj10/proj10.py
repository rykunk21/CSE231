#############################################################################
#   Computer Project 10
#
#   Design a program that allows a user to play Solitaire: Scorpion
#
#   Algorithm
#       Initialize a new tableau stock and foundation
#       If user requests move
#           check if move is valid
#           make move
#           check if user filled a column. if so, move to foundation
#           if foundation is full:
#               win and start new game
#############################################################################
# Solitaire: Scorpion


# DO NOT DELETE THESE LINES
local = False   # imports in my IDE require special import statements

if local:
    from Projects.proj10 import cards
    import random
else:
    import cards, random

random.seed(100)  # random number generator will always generate
# the same random number (needed to replicate tests)

MENU = '''     
Input options:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau (column,row) to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''


def initialize():
    """initialize the stock, foundation, and tableau"""
    stock = cards.Deck()
    stock.shuffle()

    foundation = [[], [], [], []]

    tableau = [[], [], [], [], [], [], []]  # initialize in reverse

    for i in range(7):  # deal 7 times
        for j, col in enumerate(tableau):  # deal 1 card to each column
            col.append(stock.deal())
            if (j == 0 or j == 1 or j == 2) and (i == 0 or i == 1 or i == 2):
                col[i].flip_card()  # flip top left 3x3

    return stock, tableau, foundation


def display(stock, tableau, foundation):
    """
    Display the stock and foundation at the top. Display the tableau below.
    """

    print("\n{:<8s}{:s}".format("stock", "foundation"))
    if stock.is_empty():
        print("{}{}".format(" ", " "),
              end='')  # fill space where stock would be so foundation gets printed in the right place
    else:
        print("{}{}".format(" X", "X"), end='')  # print as if face-down
    for f in foundation:
        if f:
            print(f[0],
                  end=' ')  # print first card in stack(list) on foundation
        else:
            print("{}{}".format(" ", " "),
                  end='')  # fill space where card would be so foundation gets printed in the right place

    print()
    print("\ntableau")
    print("   ", end=' ')
    for i in range(1, 8):
        print("{:>2d} ".format(i), end=' ')
    print()
    # determine the number of rows in the longest column
    max_col = max([len(i) for i in tableau])
    for row in range(max_col):
        print("{:>2d}".format(row + 1), end=' ')
        for col in range(7):
            # check that a card exists before trying to print it
            if row < len(tableau[col]):
                print(tableau[col][row], end=' ')
            else:
                print("   ", end=' ')
        print()  # carriage return at the end of each row
    print()  # carriage return after printing the whole tableau


def deal_from_stock(stock, tableau):
    """Deal the card from the stock to the tableau"""
    # expandable in case user wants to play with more than 52 cards
    for i in range(len(stock)):
        tableau[i].append(stock.deal())


def validate_move(tableau, src_col, src_row, dst_col):
    """
    Determine if the requested move is valid

    """
    try:
        usr_card = tableau[src_col][src_row]    # ensure the position exists
    except IndexError:
        return False

    if src_col == dst_col:  # cant move a card on its own column
        return False

    if len(tableau[dst_col]) == 0:  # empty columns can only accept kings
        if usr_card.rank() == 13:
            return True
        else:
            return False

    look_card = tableau[dst_col][-1]    # which card is the user moving to
    if usr_card.rank() == look_card.rank() - 1 and \
       usr_card.suit() == look_card.suit():
        return True
    else:
        return False


def move(tableau, src_col, src_row, dst_col):
    """Make a move in the game after checking if the move is valid"""

    col, row, dst = src_col, src_row, dst_col   # unnecessary line

    if validate_move(tableau, col, row, dst):
        for i in range(len(tableau[col]) - row):
            tableau[dst].append(tableau[col].pop(row))
        moved = True    # determine if a move was made
    else:
        moved = False

    if moved:
        check_for_flip(tableau)  # flip up last card in column

    return moved


def check_for_flip(tableau):
    """ flip the last card in a column if it is face down """
    for col in tableau:
        if len(col) != 0:
            if not col[-1].is_face_up():
                col[-1].flip_card()


def check_sequence(column_lst):
    """Check the column for completion"""

    if len(column_lst) != 13:  # should contain all the cards of a series
        return False
    # should have only 1 unique suit
    suits = list(dict.fromkeys([card.suit() for card in column_lst]))

    # should be in descending rank
    ranks = [card.rank() for card in column_lst]

    # move() should not allow ranks to be in incorrect order
    if len(suits) > 1 or any(ranks[i] != (ranks[i-1]-1) \
                             for i in range(1, len(ranks))):
        return False
    else:
        return True


def move_to_foundation(tableau, foundation):
    """If column is completed, move to the foundation"""
    for i, col in enumerate(tableau):
        if check_sequence(col):
            for pile in foundation:
                if len(pile) == 0:
                    pile.extend(col)
                    col.clear()  # delete the cards from the completed column
                    break
    return


def check_for_win(foundation):
    """Check if the user won"""
    if any(len(poss) != 13 for poss in foundation):
        return False
    else:
        return True


def get_option():
    '''Prompt the user for an option and check that the input has the
       form requested in the menu, printing an error message, if not.
       Return:
    D: Deal to the Tableau (one card to first three columns).
    M c r d: Move card from Tableau column,row to end of column d.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game
    '''
    option = input("\nInput an option (DMRHQ): ")
    option_list = option.strip().split()

    opt_char = option_list[0].upper()

    if opt_char == 'P':
        return ['P']

    if opt_char in 'DRHQ' and len(option_list) == 1:  # correct format
        return [opt_char]

    if opt_char == 'M' and len(option_list) == 4 and option_list[1].isdigit() \
            and option_list[2].isdigit() and option_list[3].isdigit():
        return ['M', int(option_list[1]), int(option_list[2]),
                int(option_list[3])]

    print("Error in option:", option)
    return None  # none of the above


def main():
    """Call functions based on user input. Interact with the user """

    print("\nWelcome to Scorpion Solitaire.\n")
    stock, tableau, foundation = initialize()
    display(stock, tableau, foundation)
    print(MENU)
    option_lst = get_option()
    option = option_lst[0]
    while option_lst and option_lst[0] != 'Q':
        if option == 'D':
            deal_from_stock(stock, tableau)
            display(stock, tableau, foundation)

        elif option == 'M':
            # 'col = option_lst[1] - 1' ## just having a little fun with lambda
            col, row, dst = list(map(lambda v: v - 1,
                                     [a for a in option_lst[1:]]))

            # move the card and check if moved
            if move(tableau, col, row, dst):
                move_to_foundation(tableau, foundation)
                if check_for_win(foundation):
                    print('You won!')
                    print('\nNew Game.')
                    option = 'R'  # restart already exists, set option to it
                    continue
                else:
                    display(stock, tableau, foundation)
            else:
                print("Error in move:", option, ",", option_lst[1], ",",
                      option_lst[2], ",", option_lst[3])

        elif option == 'P':  # just in case the user wants to print the tableau
            display(stock, tableau, foundation)

        elif option == 'R':
            stock, tableau, foundation = initialize()
            display(stock, tableau, foundation)
            print(MENU)

        elif option == 'H':
            print(MENU)

        elif option == 'Q':
            break

        else:
            print('Invalid option, please try again')
        option_lst = get_option()
        option = option_lst[0]

    print("Thank you for playing.")


if __name__ == '__main__':
    main()