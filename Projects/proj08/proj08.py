''' Insert heading comments here.'''
import csv


def open_file(filename=None, fp=None):
    '''Insert docstring here.'''
    if not filename:
        while True:
            try:
                filename = input("Please input a file to use: ")
                if filename == '':
                    filename = 'FOOD.txt'
                fp = open(filename, 'r')
                break
            except FileNotFoundError:
                print("Invalid filename, please try again")
                continue
        return fp
    else:
        fp = open(filename, 'r')
        return fp


def read_file(fp):
    '''Insert docstring here.'''
    file = csv.reader(fp)
    minerals_d = {}
    for line in file:
        build_dictionary(minerals_d, line)
    return minerals_d


def food_and_minerals(D):
    '''Insert docstring here.'''
    food = sorted(D.keys())
    minerals = []
    for group in D.values():
        minerals += [mineral for mineral in group]
    return food, sorted(list(set(minerals)))


def build_dictionary(D,line_list):
    '''Insert docstring here.'''
    food = line_list[0]
    minerals = set(line_list[1:])
    D[food] = minerals


def search(minerals_str, minerals_list, D,):
    """Insert docstring here."""
    if len(minerals_str.split()) == 3:
        if any(mineral not in minerals_list for mineral in
               minerals_str.split()):
            return None
    elif len(minerals_str.split('|')) == 3:
        if any(mineral not in minerals_list for mineral in
               minerals_str.split('|')):
            return None
    elif len(minerals_str.split('&')) == 3:
        if any(mineral not in minerals_list for mineral in
               minerals_str.split('&')):
            return None
    else:
        return None

    minerals = minerals_str.split('|')
    out = []
    for mineral in minerals:
        mineral = mineral.split('&')
        for food in D.keys():
            if any(val.strip().lower() not in D[food] for val in mineral):
                continue
            else:
                out.append(food)

    return sorted(list(set(out)))


def anti_anemia(D):
    '''Insert docstring here.'''
    return set([food for food in D.keys() if 'iron' in D[food]])


# Main function
def main():
    '''Insert docstring here.'''
    PROMPT = "Please enter 3 minerals using a single operand type (or q to " \
             "quit): "
    D = read_file(open_file('FOOD.txt'))
    food, minerals = food_and_minerals(D)
    print("\nWe consider these foods:")
    print(*food, sep='\n')
    print("\nWe consider these minerals:")
    print(*minerals, sep='\n')
    print()
    print('Specify three types of minerals separated by &(and) or |(or)')
    option = input(PROMPT)
    while option != 'q':
        lookup = search(option, minerals, D)
        if lookup:
            print(*lookup, sep='\n')
        else:
            print("Error in input.")
        option = input(PROMPT)

    print("\nFoods that contain iron, please eat these foods if you are anemic: ")
    print(*sorted(anti_anemia(D)), sep='\n')



#DO NOT DELETE THE NEXT TWO LINES
if __name__ == "__main__":
    main()