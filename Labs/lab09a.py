from operator import itemgetter


def build_map(in_file1, in_file2):
    in_file1.readline()
    in_file2.readline()
    data_map = {}

    # READ EACH LINE FROM FILE 1
    for line in in_file1:
    # Split the line into two words
        continent_list = line.strip().split()

        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
    # Ignore empty strings
        if continent != "" and continent not in data_map:
            data_map[continent] = dict()
            data_map[continent][country] = []
        else:
            if country != '' and country not in data_map[continent].keys():
                data_map[continent][country] = []

# READ EACH LINE FROM FILE 2

    for line in in_file2:
    # Split the line into two words
        countries_list = line.strip().split()

    # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()

    # Ignore empty strings

        # insert city (country is guaranteed to be in map)
        for continent in data_map.keys():
            if country in data_map[continent].keys():
                if city not in data_map[continent][country]:
                    data_map[continent][country].append(city)
    return data_map


def display_map(data_map):

    for continent in sorted(data_map.keys()):
        print('{}:'.format(continent))
        for i in sorted(data_map[continent].keys()):
            print('{:>10}'.format(i), end=' --> ')
            print(*sorted(data_map[continent][i]), sep=', ')


def open_file(filename=None):
    if not filename:
        try:
            filename = input("Enter file name: ")
            in_file = open(filename, "r")

        except IOError:
            print("\n*** unable to open file ***\n")
            in_file = None

        return in_file
    else:
        in_file = open(filename, "r")
        return in_file


def main():
    # YOUR CODE
    data_map = {}
    in_file1 = open_file()  # Continents with countries file:
    # continents.txt
    in_file2 = open_file()  # Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        data_map = build_map(in_file1, in_file2)  # data_map is a dictionary
        display_map(data_map)
        in_file1.close()
        in_file2.close()


if __name__ == "__main__":
    main()