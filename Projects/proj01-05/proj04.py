##########################################################
# Computer Project 04
#
# Algorithm
#   Base the code around the menu of options that the user can choose
#   Open an infinite loop to continue iteration until the user wants to stop
#   Maintain all the heavy computation to the functions then use the "main"
#   function to call the data from the user
#   Input should be prompted and then passed through the corresponding
#   function
#   Quit when the user wants to quit
###########################################################

"""If the user enters option A, the program will ask the user to enter a
numeric value N and a base number B in the range between 2 and 10 inclusive.
If N is a non-negative number and B is valid (an integer between 2 and 10),
the program will calculate and display the string representation of the
number in base B. Otherwise, the program will display an appropriate message
and re-prompt to enter the invalid input. Note that the string method
.isdigit() is useful here.

If the user enters option B, the program will ask the user to enter a
string S and a base number B in the range between 2 and 10 inclusive. If B
is valid, it will calculate and display the decimal representation of the
string. Otherwise, the program will display an appropriate message and
re-prompt to enter the invalid input

If the user enters option C, the program will ask the user to enter three
inputs: a base B1, a base B2 (both of which are between 2 and 10, inclusive)
and s_1, which is a string representing a number in base B1. If B1 and B2
are valid, it will calculate and display a string representing s_1 in base
B2. Otherwise, the program will display an appropriate message and re-prompt
to enter the invalid input.

If the user enters option D, the program should ask the user to enter two
binary strings. The program will calculate and display the sum of the two
binary numbers.

If the user enters option E, the program will ask the user to enter a
binary string. The program will compress the image and display the
run-length encoding string of the image.

If the user enters option U, the program will ask the user to enter a
binary string representing a run-length encoding string of an image. The
program will uncompress the image and display the original representation of
the image. """


def display_options():
    """ This function displays the menu of options"""

    MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             D. Display the sum of two binary numbers.
             E. Compress an image.
             U. Uncompress an image.
             M. Display the menu of options.
             X. Exit from the program.'''

    print(MENU)


def numtobase(n, b):
    """This function accepts as input a non-negative integer N (base 10,
    aka. decimal) and a “new” base B (an integer between 2 and 10
    inclusive); it should return a string representing the number N in base
    B. Your function must output the empty string when the input value of N
    is 0. (This avoids leading zeros!) """
    output = ''
    cont = True
    if n == 0:
        return ''
    while cont:
        output += str(n % b)
        if n // b == 0:
            cont = False
        else:
            n = n // b
    return output[::-1]   # instead of adding the string up in forward
    # notation, build the string backwards and return the string with a
    # negative 1 step to flip it to the correct orientation


def basetonum(s, b):
    """This function accepts as input a string S and a base B (int) where S
    represents a number in base B where B is between 2 and 10 inclusive. It
    should then return an integer in base 10 representing the same number as S.
    It should output 0 when S is the empty string. This function is the inverse
    of the previous function num_to_base()."""
    s = s[::-1]  # iterate backwards over the string again to work in reverse
    output = 0
    for i, ch in enumerate(s):  # the builtin enumerate function is useful here
        ch = int(ch)
        output += (ch * (b ** i))
    return output


def basetobase(B1, B2, s_in_B1):
    """ This function is designed to take a string in base 1 and return that
    same string in base 2. Both base 1 and base 2 can be determined by the
    user. """

    actual_s1 = basetonum(s_in_B1, B1)  # instead of completing a new
    # function, use this function to call a previous function and then alter
    # the data a little bit
    return numtobase(actual_s1, B2)


def addbinary(s, t):
    """ This function adds binary numbers together and returns a string of
    the added binary strings"""

    s = int(basetobase(2, 10, s))
    t = int(basetobase(2, 10, t))

    return str(bin(s + t))[2:]  # using the bin() function, we can convert
    # any number into binary and then remove the first two characters (0b)
    # to convert any number to binary. in this case its s + t


def compress(s):
    """ This function returns a string of the most concise 1 byte value form
    of the string in the format: first = color, remaining 7 = quantity; use
    the .zfill() method with the bin() function reduce the amount of code
    ( this function makes a byte sized string (; )"""
    if len(s) < 1:  # check if the string is empty and return empty string if
        # True
        return ''
    output = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            output += s[i - 1] + str(bin(count))[2:].zfill(7)
            count = 1
    output += s[-1] + str(bin(count))[2:].zfill(7)
    return output


def uncompress(s):
    """ This function returns the original string via decoding the run
    length encoded version of the image. We need to note that the the
    encoded string is represented as s[0] == color and s[1:8] == binary
    representation of the count of the color. Using this information we can
    simply reverse the effect of run length encoding of the image """
    output = ''
    curr = ''
    val = ''
    for i in range(len(s)):
        if i == 0:
            curr = s[i]
        elif i % 8 == 0:
            val = basetonum(val, 2)
            output += curr * val
            val = ''
            curr = s[i]
        else:
            val += s[i]
    val = basetonum(val, 2)
    output += curr * val
    return output


def assign_bool(s):
    """ this function is used to assign True or False when a user puts inputs
    yes or no. This function will also return None if the user inputs
    anything besides yes or no, and we can use this return value to check
    the user input infinitely until we get yes or no, saving a ton of
    redundant coding"""
    s = s.lower()
    if s == 'yes':
        s = True
    elif s == 'no':
        s = False
    else:
        print("Invalid input. Try again.")
        return None
    return s


def valid_base(prompt):
    while True:
        b = input(prompt)
        if not b.isdigit():
            print("\n\tError: {} was not a valid integer between 2 and 10 "
                  "inclusive.".format(b))
            continue
        else:
            b = int(b)
        if not 2 <= b <= 10:
            print("\n\tError: {} was not a valid integer between 2 and 10 "
                  "inclusive.".format(b))
            continue
        else:
            break
    return b


def valid_number():
    while True:
        n = input("\n\tEnter N: ")
        if not n.isdigit():
            print("\n\tError: {} was not a valid "
                  "non-negative integer.".format(n))
            continue
        else:
            n = int(n)
        if not n >= 0:
            print("\n\tError: {} was not a valid "
                  "non-negative integer.".format(n))
            continue
        else:
            break
    return n


def main():
    import math
    BANNER = '''
            .    .        .      .             . .     .        .          .          .
             .                 .                    .                .
      .               A long time ago in a galaxy far, far away...   .
                  .   A terrible civil war burns throughout the  .        .     .
                     galaxy: a rag-tag group of freedom fighters   .  .
         .       .  has risen from beneath the dark shadow of the            .
    .        .     evil monster the Galactic Empire has become.                  .  .
        .      Outnumbered and outgunned,  the Rebellion burns across the   .    .
    .      vast reaches of space and a thousand-thousand worlds, with only     .
        . their great courage - and the mystical power known as the Force -
         flaming a fire of hope. a                                    .

                  .------.
                .'::::::' `.
                |: __   __ |
                | <__] [__>|
                `-.  __  .-'
                  | |==| |
                  | |==| |
               __.`-[..]-`\__
        _.--:``      ||   _``:::--._
       | |  |.      .:'  (o) ::|  | |
       |_|  |::..  // _       :|  |_|
        ===-|:``` // /.\       |-===
       |_| `:___//_|[ ]|_____.' |_| )
        l=l   |\V/_=======_==|   l=l/
      .-l=l   |`'==/=="======|  /|.:
      | l l   |=="======\=_==| `-T l
      `.l_l   |==============|   l_l
        [_]  [__][__]____[_]__]  [_]
        \\\ .'.--.- --   --. .`. |||.
        \\\\| |  |    |    |  || ||||
         \\\\   .'    |    |  |`.||||   
          \\\\  |  LS |    `.   |||||     



      ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                       and there is only one line of defense remaining        
                       It is up to you to stop the invasion and save the planet~~    

        '''

    print(BANNER)
    cont = True

    display_options()
    while cont:
        acceptable_options = 'abcdeumx'
        option = input("\n\tEnter option: ").lower()
        if option not in acceptable_options or len(option) > 1:
            print('Error: unrecognized option [N]\n')
            display_options()
            continue
        if option == 'm':
            display_options()

        elif option == 'a':

            n = valid_number()
            b = valid_base("\n\tEnter Base: ")
            print("\n\t {} in base {}: {}".format(n, b, numtobase(n, b)))

        elif option == 'b':

            S = input("\n\tEnter string number S: ")
            b = valid_base('\n\tEnter Base: ')
            print("\n\t {} in base {}: {}".format(S, b, basetonum(S, b)))

        elif option == 'c':

            B1 = valid_base("\n\tEnter base B1: ")
            B2 = valid_base("\n\tEnter base B2: ")
            S = input("\n\tEnter string number S: ")

            print("\n\t {} in base {} is {} in base {}...".format(S, B1,
                                                                  basetobase(
                                                                      B1, B2,
                                                                      S), B2))

        elif option == 'd':

            binary_string_1 = input("\n\tEnter the first string number: ")
            binary_string_2 = input("\n\tEnter the second string number: ")
            print()
            print()
            print("\n\tThe sum:  {}".format(addbinary(binary_string_1,
                                                      binary_string_2)))

        elif option == 'e':

            s = input("\n\tEnter a binary string of an image: ")
            print("\n\t Original image: {}".format(s))
            print("\n\t Run-length encoded image: {}".format(compress(s)))

        elif option == 'u':

            s = input("\n\tEnter a run-length encoded string of an image: ")
            print("\n\t Run-length encoded image: {}".format(s))
            print("\n\t Original image: {}".format(uncompress(s)))

        elif option == 'x':
            cont = False

    print('May the force be with you.')


if __name__ == "__main__":
    main()
