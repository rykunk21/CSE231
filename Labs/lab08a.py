import string
from operator import itemgetter


def add_word(word_map, word):
    """ Build a dictionary all the words and their counts """
    # initializes a new key value pair if one doesnt already exist
    if word not in word_map:
        word_map[word] = 0

    # adds one to the the key's value if the key already exists
    word_map[word] += 1


def build_map(in_file, word_map):
    """ Find the counts of every word and send to add word function """
    for line in in_file:

        # make a list of all the lines in the file
        word_list = line.split()

        for word in word_list:
            if not any(let.isalpha() for let in word):
                continue
            # iterate of the list one word at a time
            word = word.strip().strip(string.punctuation).lower()
            add_word(word_map, word)


def display_map(word_map):
    """ Print the sorted data by sorting alphabetically then numerically """
    word_list = list()

    # add the dictionary to a list
    for word, count in word_map.items():
        word_list.append((word, count))

    # sort a sorted version of the list itself to sort by name then count
    freq_list = sorted(sorted(word_list), key=itemgetter(1), reverse=True)

    print("\n{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def display_specific(word_map):
    """ Display the count of specific words"""
    word_list = list()
    # use list comprehension to make a list of specific words
    value = [val.lower() for val in input('Enter a word(s) to count '
                                          'separated by a space:\n--> '
                                          '').split()]

    # delete repeating values
    value = list(dict.fromkeys(value))

    # Determines if the word is in the desired word
    for word, count in word_map.items():
        if any(word == val for val in value):
            value = [x for x in value if x != word]
            word_list.append((word, count))
    for val in value:
        word_list.append((val, 0))

    freq_list = sorted(sorted(word_list), key=itemgetter(1), reverse=True)
    print("\n{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def open_file():
    """ opens a file and returns a file pointer to be read by build_map """
    try:
        in_file = open(input('Enter file name: '), "r")

    except IOError:
        print("\n*** unable to open file ***\n")
        in_file = None

    return in_file


word_map = dict()
in_file = None
while in_file is None:
    in_file = open_file()

build_map(in_file, word_map)
display_map(word_map)
in_file.close()

"""
while True:
    ask = input('\n\nWould you like to display specific words? ['
                'y/n]\n--> ').lower()
    if ask == 'y':
        display_specific(word_map)
        continue
    elif ask == 'n':
        break
    else:
        print('Unrecognized command, please try again')
        continue
"""