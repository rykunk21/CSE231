def open_file(filename):

    with open(filename, 'r') as file:
        file.readline()
        lines = [line.strip() for line in file.readlines()]
    return lines


def run_total(data, lines):
    for line in sorted(lines):
        name, score = line.split()
        if name in data.keys():
            data[name] += int(score)
        else:
            data[name] = int(score)
    return data


def sort_data(data):
    return sorted(data.items())


def user_continue():
    return True if input('\nDo you wish to add more data? ').lower() == 'y' \
        else False


def main():
    data = {}
    data = run_total(data, open_file('data1.txt'))
    # cont = user_continue()

    # while cont
    data = run_total(data, open_file('data2.txt'))
        # cont = user_continue()

    print("{:10s} {:<10s}".format('Name', 'Total'))
    for i in sort_data(data):
        print("{:10s} {:<10d}".format(*i))


main()
