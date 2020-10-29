import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction',
              'Leisure/hospitality', 'Manufacturing']


def read_file(fp):
    """ Docstring """
    for i in range(3):
        next(csv.reader(fp))

    return [line for line in csv.reader(fp) if line[0] != '']


def get_totals(L):
    """ Returns the total """
    first = clean_string(L[0][1])
    total = 0
    for i, line in enumerate(L):
        if i == 0:
            continue
        else:
            total += int(clean_string(line[1]))
    return int(first), int(total)


def get_industry_counts(L):
    """ Count how many industries are populated with immigrants by state """
    industry_counts = []
    occurances = []
    M = L[1:]
    for line in M:
        occurances.append(line[9])
    for line in M:
        if line[9] != '-':
            if not any(line[9] in here for here in industry_counts):
                industry_counts.append([line[9], occurances.count(line[9])])
            else:
                continue

    return sorted(industry_counts, key=itemgetter(1), reverse=True)


def get_largest_states(L):
    """ Return the states that have higher immigrant populations """

    user_out = []
    for i, line in enumerate(L):
        if i == 0:
            summative = float(clean_string(line[2]))
        else:
            if float(clean_string(line[2])) > summative:
                user_out.append(line[0])
    return user_out


def clean_string(s):
    s_out = ''
    for ch in s:
        if not ch.isdigit():
            continue
        else:
            s_out += ch
    return s_out


def main():
    fp = open("../immigration.csv")
    L = read_file(fp)
    us_pop, total_pop = get_totals(L)
    a = 1
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)

    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n', ' ')
            print(state)

    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry", "count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0], tup[1]))


if __name__ == "__main__":
    main()
