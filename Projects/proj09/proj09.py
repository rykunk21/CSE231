import csv
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

# link
# https://www.kaggle.com/unsdsn/world-happiness


def open_file(year=None):
    """
    Opens a file from a year in the format (year + .csv)

    :param year: str
    :return: file pointer
    """
    try:
        fp = open('{}.csv'.format(year))
        return fp
    except FileNotFoundError:
        return None


def build_dictionary(fp):
    """
    Iterates over the file and returns

    :param fp: file pointer
    :return: dict
    """
    # use the next function to skip a line, with a default of None
    next(csv.reader(fp), None)
    data = dict()   # initialize the data for return
    # initialize a dictionary with the indices of the data
    assn = {
        'Region': 1,
        'Country': 0,
        'Happiness Rank': 2,
        'Happiness Score': 3,
        'Economy': 5,
        'Trust': 9,
        'Family': 6,
        'Health': 7,
        'Freedom': 8
    }

    for line in csv.reader(fp):
        # don't init a new region if it already exists
        if line[assn['Region']] not in data.keys():
            data[line[assn['Region']]] = dict()
        try:    # test if data is available
            data[line[assn['Region']]].update(dict({line[assn['Country']]:
                                              ((int(line[assn['Happiness Rank']]),
                                                   float(line[assn['Happiness '
                                                               'Score']])),
                                                  (float(line[assn['Economy']]),
                                                   float(line[assn['Trust']])),
                                                  (float(line[assn['Family']]),
                                                   float(line[assn['Health']]),
                                                   float(line[assn[
                                                       'Freedom']])))}))
        except ValueError:
            continue

    return data


def combine_dictionaries(year, subD, superD):
    """ Add a year into an existing super dictionary """
    superD[year] = subD
    return superD


def search_by_country(country, superD, print_boolean):
    """
    this function will gather relevant data from superD param and display
    it to the console if print_boolean. Else return list of data

    :param country: str
    :param superD: dict
    :param print_boolean: Bool
    """
    print_deny = []
    # check the superD for the country values:
    data = []   # initialize a place to add data
    for year in superD.keys():
        for region in superD[year]:
            for __country in superD[year][region]:
                if __country == country:
                    data = [tup for tup in superD[year][region][country]]
                else:
                    continue
                break
        if len(data) < 1:   # if country wasn't found, keep iterating
            continue
        else:   # initialize data to be printed or returned
            rank = int(data[0][0])
            score = float(data[0][1])
            family = float(data[2][0])
            health = float(data[2][1])
            freedom = float(data[2][2])
        if print_boolean:
            print()
            print('{:<10s}{:<5d}'.format('Year:', year))
            print('{:<10s}{:<s}'.format('Country:', country))
            print('{:<10s}{:<5d}'.format('Rank:', rank))
            print('{:<10s}{:<5.2f}'.format('Score:', score))
            print('{:<10s}{:<5.2f}'.format('Family:', family))
            print('{:<10s}{:<5.2f}'.format('Health:', health))
            print('{:<10s}{:<5.2f}'.format('Freedom:', freedom))
            print('-' * 20)
        else:
            print_deny.append((score, family, health, freedom))
    if len(print_deny) > 1:   # check if print didn't execute
        return print_deny


def top_10_ranks_across_years(superD, year1, year2):
    """
    Search the data for countries statistics in a multiple years. This data
    will be passed to print_ranks() function which will print the data to
    the console

    :param superD: dict
    :param year1: str
    :param year2: str
    :return: tuple(list, list)
    """

    # init place to store data
    year1list = []
    year2list = []
    # function out will end up storing the year2list in correct order
    function_out = []

    # simple loop to get the sorted top 10 for year 1
    for region in superD[year1]:
        for country in superD[year1][region]:
            year1list.append((country, superD[year1][region][country][0][0]))
    year1list = sorted(year1list, key=itemgetter(1))[:10]

    # grab year2 data, we are not worried about the countries yet, just rank
    for region in superD[year2]:
        for country in superD[year2][region]:
            year2list.append((country, superD[year2][region][country][0][0]))

    # iterate over the countries in year1, and append the data to function
    # out upon a match. This will preserve accuracy and order
    for entry in year1list:
        for exist in year2list:
            if exist[0] == entry[0]:
                function_out.append(exist)

    return year1list, function_out


def print_ranks(superD, list1, list2, year1, year2):
    """
    Prints the data from top_10_ranks_across_years() to the console

    :param superD: dict
    :param list1: list
    :param list2: list
    :param year1: str
    :param year2: str
    :return:
    """
    # print header line
    print('{:<15s} {:>7s} {:>7s} {:>12s}'.format('Country', str(year1),
                                                 str(year2),
                                                 'Avg.H.Score'))
    # grab values and indices
    for i, entry in enumerate(list1):
        country, rank1 = entry
        rank2 = list2[i][1]  # get corresponding index
        deny = search_by_country(country, superD, False)
        score = (deny[0][0] + deny[1][0]) / 2
        # print line
        print('{:<15s} {:>7d} {:>7d} {:>12.2f}'.format(country, rank1,
                                                       rank2, score))


def prepare_plot(country1, country2, superD):
    """
    initialize data for bar plot function to plot

    :param country1: str
    :param country2: str
    :param superD: dict
    :return: tup(tup, tup) containing search
    """
    tup1 = search_by_country(country1, superD, False)
    tup2 = search_by_country(country2, superD, False)

    return tuple(tup1[0]), tuple(tup2[0])


def bar_plot(country1, country2, countrylist1, countrylist2):
    """
    plot the data from prepare plot

    :param country1: str
    :param country2: str
    :param countrylist1: list
    :param countrylist2: list
    :return: plot
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    N = 4
    ind = np.arange(N)
    width = 0.25

    rects1 = ax.bar(ind, countrylist1, width,
                    color='black',
                    error_kw=dict(elinewidth=2, ecolor='blue'))

    rects2 = ax.bar(ind + width, countrylist2, width,
                    color='red',
                    error_kw=dict(elinewidth=2, ecolor='red'))

    ax.set_xlim(-width, len(ind) + width)
    ax.set_ylabel('Quantity')
    ax.set_title('Comparison between the two countries')
    xTickMarks = ['Happiness Sc.', 'Family', 'Health', 'Freedom']
    ax.set_xticks(ind + width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=0, fontsize=10)

    ax.legend((rects1[0], rects2[0]), (country1, country2))
    plt.show()


def check(country, superD):
    """
    checks if the country is in the superD
    :param country: str
    :param superD: dict
    :return: str or None
    """
    for year in superD:
        for region in superD[year]:
            for country__ in superD[year][region]:
                if country__ == country:
                    return country
    return None


def main():
    """
    Interaction with the user to display a menu and divert options to
    functions

    """

    BANNER = '''
                    __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
    oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
    oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
    oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
    *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
    *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
        *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
          *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
             *OOOOOOOOo           oOOOOOOOO*      
                 *OOOOOOOOOOOOOOOOOOOOO*    
                      ""ooooooooo""
    '''

    MENU = '''
    1. Search by country
    2. Top 10 countries
    3. Compare countries
    x. Exit 
    :'''
    print(BANNER)



    superD = {}  # initialize superD for an argument

    # gather desired years
    years = [year.strip() for year in input('Input Years '
                                            'comma-separated as '
                                            'A,B: ').split(',')]

    for year in years:
        print('Opening Data file for year {}: '.format(year))
        superD[int(year)] = build_dictionary(open_file(year))


    user_choice = input(MENU)

    while user_choice.lower() != 'x':

        if user_choice == '1':

            country = check(input("[ ? ] Please specify the country: "),
                            superD)
            while not country:
                print("[ - ] Incorrect input. Try again.")
                country = check(input("[ ? ] Please specify the country: "),
                                superD)
            search_by_country(country, superD, True)

        elif user_choice == '2':
            l1, l2 = top_10_ranks_across_years(superD, int(years[0]),
                                               int(years[1]))
            print_ranks(superD, l1, l2, int(years[0]), int(years[1]))

        elif user_choice == '3':
            countries = input("[ ? ] Please specify the two countries "
                                "(A,"
                              "B): ").split(',')
            for country in countries:
                country.strip()


            print('{:<20s} {:<9s} {:<8s} {:<8s} {:<8s}'.format("\nCountry",
                                                               "Hap.Score",
                                                               "Family",
                                                               "Life Ex.",
                                                               "Freedom"))
            for country in countries:
                data = search_by_country(country, superD, False)
                score = data[0][0]
                family = data[0][1]
                health = data[0][2]
                freedom = data[0][3]
                print("{:<20s} {:<9.2f} {:<8.2f} {:<8.2f} {:<8.2f}".format(
                    country, score, family, health, freedom))

            plot = input("[ ? ] Plot (y/n)? ")
            if plot.lower() == 'y':
                l1, l2 = prepare_plot(countries[0], countries[1], superD)
                bar_plot(countries[0], countries[1], l1, l2)

        elif user_choice.lower() == 'c':  # entry to change years
            years = [year.strip() for year in input('Input Years '
                                                    'comma-separated as '
                                                    'A,B: ').split(',')]
            superD = {}  # initialize superD for an argument

            for year in years:
                print('Opening Data file for year {}: '.format(year))
                superD[int(year)] = build_dictionary(open_file(year))



        else:
            print("[ - ] Incorrect input. Try again.")
        user_choice = input(MENU)
if __name__ == '__main__':
    main()
