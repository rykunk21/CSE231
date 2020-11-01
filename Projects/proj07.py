#########################################################
#
#
#########################################################

# import pylab as py
import csv

MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
          'NOV', 'DEC']


def open_file():
    "Insert DocString here."
    while True:
        try:
            #  input("Enter filename: "
            fp = open('earthquake_data.csv', 'r')
            break
        except FileNotFoundError:
            print("\nFile is not found! Please Try Again!")
            continue
    return fp


def read_file(fp):
    "tup = (month, magnitude, location, latitude, longitude)."
    next(csv.reader(fp))
    file = [line for line in csv.reader(fp)]
    for i, line in enumerate(file):
        line = [x if x != '' else 0 for x in line]
        ints = [line[2], line[3], line[23], line[25], line[27]]
        floats = [line[9], line[20], line[21], line[29]]
        try:
            year, month, deaths, missing, injuries = map(int, ints)
            magnitude, latitude, longitude, damages = (map(float, floats))
            location = line[19]
            tup = (year, month, magnitude, location, latitude,
                   longitude, deaths, missing, injuries, damages)
            file[i] = tup
        except ValueError:
            continue

    file = [x for x in file if isinstance(x, tuple)]

    return file


def get_damage_data(data, year):
    """This function iterates through the list of earthquake tuples
and returns a list of the earthquakes that occurred in the given year. This function
extracts the month, location (truncated to the first 40 characters), the number of deaths,
missing, injuries, and damages from earthquakes in a single year into a tuple in that
order:
tup = (month,location,deaths,missing,injuries,damages)."""
    function_out = []
    for i, line in enumerate(data):
        if line[0] == year:
            tup = (line[1], line[3][:40], line[6], line[7], line[8], line[9])
            function_out.append(tup)

    return function_out


def get_quake_data(data, year):
    "Insert DocString here."
    function_out = []
    for i, line in enumerate(data):
        if line[0] == year:
            tup = (line[1], line[2], line[3], line[4], line[5])
            function_out.append(tup)

    return function_out  # insert your code here


def summary_statistics(data, year_start, year_end):
    """ (year, (total_deaths, total_missing, total_injured))"""
    if year_end < year_start:
        print("\nYear range [{},{}] is invalid!".format(year_start, year_end))
        return []
    function = sorted([x for x in data if year_start <= x[0] <= year_end])
    count = {}
    damage = {}
    casualties = {}
    for year in function:
        if year[0] in count.keys():
            count[year[0]] += 1
            casualties[year[0]][0] += year[6]
            casualties[year[0]][1] += year[7]
            casualties[year[0]][2] += year[8]
        else:
            casualties[year[0]] = [0, 0, 0]
            count[year[0]] = 1
        if year[0] in damage.keys():
            damage[year[0]] += year[-1]
        else:
            damage[year[0]] = 0

    for key in casualties.keys():
        casualties[key] = tuple(casualties[key])

    return list(map(list, [count.items(), damage.items(),
                           casualties.items()]))


def display_damage_data(L, year):
    """
    for i, val in enumerate(data)

    """

    print('\n{:^98s}'.format("Earthquake damage costs in {}".format(year)))
    print("{:8s}{:40s}{:>12s}{:>12s}{:>12s}{:>14s}".format("Month",
                                                           "Location",
                                                           "Deaths",
                                                           "Missing",
                                                           "Injuries",
                                                           "Damage"))
    print("{:8s}{:40s}{:>12s}{:>12s}{:>12s}{:>14s}".format("", "", "", "", "",
                                                           "(Millions)"))
    data = list(get_damage_data(L, year))
    deaths, missing, injuries, damage = 0, 0, 0, 0
    for i, val in enumerate(data):
        val = list(val)
        val[0] = MONTHS[val[0]-1]
        val[1] = val[1][:40]
        deaths += val[2]
        missing += val[3]
        injuries += val[4]
        damage += val[5]
        print("{:<8s}{:40s}{:12,d}{:12,d}{:12,d}{:14,.2f}".format(*val))

    print('\n{:<8s}{:40s}{:12,d}{:12,d}{:12,d}{:14,.2f}'.format('Total', '',
                                                                deaths,
                                                                missing,
                                                                injuries,
                                                                damage))


def display_quake_data(L, year):
    """
    (month, magnitude, location, latitude, longitude)
    "{:8s}{:10s}{:40s}"
    {:<8s}{:<10.2f}{:40s}"""


    data = get_quake_data(L, year)
    print("Earthquake magnitudes and locations in {}".format(year))
    print("{:8s}{:10s}{:40s}".format("Month", "Magnitude", "Location"))
    for val in data:
        print('{:<8s}{:<10.2f}{:40s}'.format(MONTHS[val[0]-1], val[1], val[2]))


def display_summary(quakes, costs, casualties):
    "Insert DocString here."
    print("\nNumber of earthquakes and costs per year")
    t_quakes, t_costs, t_casualties = 0, 0, 0
    for i, val in enumerate(quakes):
        year, quakes = val[0], val[1]
        t_quakes += quakes
        t_costs += costs[i][1]
        print("{:<5d}{:10,d}{:12,.2f}".format(year, quakes, costs[i][1]))
    print("\n{:<5s}{:10,d}{:12,.2f}".format('Total', t_quakes, t_costs))
    print("\nTotal Casualties")
    deaths, missing, injured = 0, 0, 0
    for val in casualties:
        deaths += val[1][0]
        missing += val[1][1]
        injured += val[1][2]
    total = deaths + missing + injured
    print("{:10s}{:10d}{:10,.2f}%".format('Deaths', deaths,
                                          (deaths/total)*100))
    print("{:10s}{:10d}{:10,.2f}%".format('Missing', missing,
                                          (missing/total)*100))
    print("{:10s}{:10d}{:10,.2f}%".format('Injured', injured,
                                          (injured/total)*100))


def plot_intensity_map(year, quake_data):
    '''
        This function plots the map of the earthquake locations for the
        selected year. This function is provided in the skeleton code.

        Parameters:
            year (string): The year key for the data to plot
            size (int): Number of earthquakes that occured in the selected year

            coordinates (list): List of (latitude,longitude) coordinates for
                                the trajectory of each earthquake that occured
                                in the selected year.

        Returns: None
    '''

    # The the RGB list of the background image.
    img = py.imread("world-map.jpg")

    # Set the max values for the latitude and longitude of the map
    max_longitude, max_latitude = 180, 90

    # Set the background image on the plot
    py.imshow(img, extent=[-max_longitude, max_longitude, -max_latitude,
                           max_latitude])

    # Show the atlantic ocean region
    py.xlim((-max_longitude, max_longitude))
    py.ylim((-max_latitude, max_latitude))

    # build the x,y coordinates map
    lst = list(zip(*quake_data))
    lat, lon, mag = lst[3], lst[4], lst[1]

    area = ([(1.0 * p) ** 2 for p in mag])

    # plot the scatter plot
    scatter = py.scatter(lon, lat, s=area, c=mag, cmap='seismic')
    py.colorbar(scatter)

    # Set the labels and titles of the plot
    py.xlabel("Longitude (degrees)")
    py.ylabel("Latitude (degrees)")
    py.title("Earthquake Magnitude points for {}".format(year))
    py.show()  # show the full map


def plot_bar(L, title, x_label, y_label):
    '''
        This function receives a list of x,y values.

        Parameters
            L (list):
            title (str):
            x_label (str):
            y_label (str):

        Returns
            None
    '''

    # count the earthquakes per month
    total = [0] * 12
    for i in L:
        total[i[0] - 1] += 1

    py.title(title)
    py.xlabel(x_label)
    py.ylabel(y_label)
    py.xticks(range(12), MONTHS)
    py.bar(range(12), total)
    py.show()


def plot_line(L, title, x_label, y_label):
    '''
        This function receives a list of x,y values.

        Parameters
            L (list):
            title (str):
            x_label (str):
            y_label (str):

        Returns
            None
    '''
    res = list(zip(*L))

    py.title(title)
    py.xlabel(x_label)
    py.ylabel(y_label)
    py.xticks(range(len(res[0])), [str(r) for r in res[0]], rotation=90)
    py.plot(range(len(res[0])), res[1], marker="o")

    py.show()


def plot_pie(L, title):
    '''
        This function receives a list of x,y values.

        Parameters
            L (list):
            title (str):

        Returns
            None
    '''
    #            L[2].append((y,(deaths,missing,injured)))
    deaths = sum([t[0] for y, t in L])
    missing = sum([t[1] for y, t in L])
    injured = sum([t[2] for y, t in L])
    total = deaths + missing + injured
    d = deaths / total
    m = missing / total
    i = injured / total
    L = [["deaths", d], ["missing", m], ["injuries", i]]

    res = list(zip(*L))

    py.title(title)
    py.pie(res[1], labels=res[0], autopct='%.1f%%')
    py.show()


def get_year(year):
    try:
        year = int(year)
        return year
    except ValueError:
        print("\nYear input '{}' is incorrect!")
        return


def main():
    '''
        This program will show damages caused by an earthquakes in a year.
        Also, it will plot the intensity of all earthquakes observed in a year.

    '''

    MENU = '''\nEarthquake data software

        1) Visualize damage data for a single year
        2) Visualize earthquakes magnitudes for a single year
        3) Visualize number of earthquake and their damages within a range of years
        4) Exit the program

        Enter a command: '''
    file = read_file(open_file())

    option = input(MENU)
    while True:
        if option == '1':
            year = get_year(input("Enter a year: "))
            display_damage_data(file, year)
            if input("Do you want to plot (y/n)? ").lower() == 'y':
                title = "Monthly earthquakes in {}".format(year)
                xlabel = 'months'
                ylabel = 'earthquakes'
                plot_bar(get_damage_data(file, year), title, xlabel, ylabel)
            option = input(MENU)
            continue
        elif option == '2':
            year = get_year(input("Enter a year: "))
            display_quake_data(file, year)
            if input("Do you want to plot (y/n)? ").lower() == 'y':
                plot_intensity_map(str(year), file)
            option = input(MENU)
            continue
        elif option == '3':
            start = get_year(input("\nEnter start year: "))
            end = get_year(input("Enter end year: "))
            start, end = map(int, [start, end])
            display_summary(*summary_statistics(file, start, end))
            option = input(MENU)
            continue
        elif option == '4':
            break
        else:
            print("\nOption '{}' is invalid! Please Try Again!".format(option))
            option = input(MENU)

    print("\nThank you for using this program!")


if __name__ == "__main__":
    main()
