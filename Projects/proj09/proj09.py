import csv
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt

def open_file(year=None):
    """
    Opens a file from a year in the format (year + .csv)

    :param year: a year from the user
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

    :param fp: file pointer given from the open_file function
    :return: dict of data
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
        data[line[assn['Region']]].update(dict({line[assn['Country']]:
                                          ((line[assn['Happiness Rank']],
                                               line[assn['Happiness Score']]),
                                              (line[assn['Economy']],
                                               line[assn['Trust']]),
                                              (line[assn['Family']],
                                               line[assn['Health']],
                                               line[assn['Freedom']]))}))
    return data


def combine_dictionaries(year, subD, superD):
    ''' Docstring '''
    superD[year] = subD
    return superD


def search_by_country(country, superD, print_boolean, years):
    """
    this function will gather relevant data from superD param and display
    it to the console if print_boolean. Else return list of data

    :param country: string containing the country name
    :param superD: dictionary of data
    :param print_boolean: True or False
    """
    # check the superD for the country values:
    data = []
    for region in superD.keys():
        for __country in superD[region]:
            if __country == country:
                data = [tup for tup in superD[region][country]]
            else:
                continue
            break
        if len(data) < 1:
            continue
        else:
            break

    print_deny = []
    for year in years:
        rank = int(data[0][0])
        score = float(data[0][1])
        family = float(data[2][0])
        health = float(data[2][1])
        freedom = float(data[2][2])
        if print_boolean:
            print('{:<10s}{:<5d}'.format('Year:', year))
            print('{:<10s}{:<s}'.format('Country:', country))
            print('{:<10s}{:<5d}'.format('Rank:', rank))
            print('{:<10s}{:<5.2f}'.format('Score', score))
            print('{:<10s}{:<5.2f}'.format('Family:', family))
            print('{:<10s}{:<5.2f}'.format('Health:', health))
            print('{:<10s}{:<5.2f}'.format('Freedom:', freedom))
            print('-'*20)
        else:
            print_deny.append((score, family, health, freedom))
    return print_deny


def top_10_ranks_across_years(superD, year1, year2):
    ''' Docstring '''
    pass  # replace with your code


def print_ranks(superD, list1, list2, year1, year2):
    ''' Docstring '''
    pass  # replace with your code


def prepare_plot(country1, country2, superD):
    ''' Docstring '''
    pass  # replace with your code


def bar_plot(country1, country2, countrylist1, countrylist2):
    ''' Bar plot comparing two countries.'''
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


def main():
    ''' Docstring '''

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

    superD = {}

    # YOUR CODE TO READ THE FILES AND BUILD SUPER DICTIONARY

    d = build_dictionary(open_file('2015'))

    print(search_by_country('Ireland', d, False, [2015]))

    user_choice = input(MENU)

    while user_choice.lower() != 'x':
        # YOUR CODE TO RESPOND TO USER CHOICES
        pass  # replace with your code
        #        else:
        #            print("[ - ] Incorrect input. Try again.")
        user_choice = input(MENU)



if __name__ == '__main__':
    main()

