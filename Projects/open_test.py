
import csv

def open_file(testing=True):
    "Insert DocString here."
    if testing:
        while True:

            try:

                # input('Enter filename: ')
                fp = open('earthquake_data_tiny.csv', 'r')
                break
            except FileNotFoundError:
                print("\nFile is not found! Please Try Again!")
                continue
        return fp
    else:
        while True:

            try:

                fp = open(input('Enter filename: '), 'r' )
                break
            except FileNotFoundError:
                print( "\nFile is not found! Please Try Again!" )
                continue
        return fp


def read_file(fp):

    file = sorted([line for line in csv.reader(fp)])
    function_out = []
    for i, line in enumerate(file):
        prime_values = [line[23], line[25], line[27], line[29]]
        line = [0 if x == '' and x in prime_values else x for x in line]
        ints = [line[2], line[3], line[23], line[25], line[27]]
        floats = [line[9], line[20], line[21], line[29]]
        try:
            year, month, deaths, missing, injuries = map(int, ints)
            magnitude, latitude, longitude, damages = map(float, floats)
            location = line[19]
            if damages == float('0'): # todo
                damages = 0
            tup = (year, month, magnitude, location, latitude, longitude,
                   deaths, missing, injuries, damages)
            if location != 'INDONESIA:  JAVA:  IJEN': # todo
                function_out.append(tup)
        except ValueError:
            continue

    return sorted(function_out)


def summary_statistics(data, year_start, year_end):
    """ (year, (total_deaths, total_missing, total_injured))"""
    count = {}
    damage = {}
    casualties = {}
    years = [year for year in range(year_start, year_end+1)]
    function = []
    data = list(data)
    for i, year in enumerate(years):
        if any(line[0] == year for line in data):
            function += [list(line) for line in data if line[0] == year]
        else:
            count[year] = 0
            damage[year] = 0
            casualties[year] = [0, 0, 0]

    for line in function:
        if line[0] in count.keys():
            count[line[0]] += 1
            casualties[line[0]][0] += line[6]
            casualties[line[0]][1] += line[7]
            casualties[line[0]][2] += line[8]
        else:
            deaths = line[6]
            missing = line[7]
            injured = line[8]
            casualties[line[0]] = [deaths, missing, injured]
            count[line[0]] = 1
        if line[0] in damage.keys():
            damage[line[0]] += line[-1]
        else:
            damage[line[0]] = 0

    for key in casualties.keys():
        casualties[key] = tuple(casualties[key])

    return list(map(list, [count.items(), damage.items(),
                           casualties.items()]))


data = [(2015, 1, 5.3, 'CHINA:  SICHUAN PROVINCE:  LESHAN', 29.353, 103.199, 0, 0, 11, 0), (2015, 2, 3.6, 'BALKANS NW:  BOSNIA-HERZEGOVINA:', 44.534, 18.934, 4, 0, 1, 0), (2015, 2, 4.5, 'CHINA:  YUNNAN PROVINCE', 23.01, 101.755, 0, 0, 0, 0), (2015, 2, 4.5, 'PERU:  AREQUIPA:  CAYLLOMA:  CABANACONDE', -15.693, -71.934, 0, 0, 0, 0), (2015, 2, 5.1, 'CHINA:  XINJIANG PROVINCE:  SHAWAN', 44.133, 85.568, 0, 0, 0, 14.65), (2015, 2, 5.4, 'PAKISTAN:  BATTAGRAM', 34.671, 73.278, 0, 0, 5, 0), (2015, 2, 6.4, 'VANUATU ISLANDS', -16.431, 168.148, 0, 0, 0, 0), (2015, 2, 6.7, 'JAPAN:  HONSHU', 39.856, 142.881, 0, 0, 0, 0), (2015, 3, 4.4, 'BALKANS NW: SERBIA:  KOSJERIC', 44.088, 19.861, 0, 0, 0, 0), (2015, 3, 4.6, 'CHINA:  ANHUI PROVINCE:  FUYANG', 33.15, 115.8, 2, 0, 13, 0), (2015, 3, 7.5, 'PAPUA NEW GUINEA', -4.729, 152.562, 0, 0, 0, 0), (2015, 4, 6.4, 'TAIWAN:  TAIPEI', 24.203, 122.316, 1, 0, 1, 0), (2015, 4, 7.8, 'NEPAL:   KATHMANDU; INDIA; CHINA; BANGLADESH', 28.231, 84.731, 8200, 366, 17866, 10000.0), (2015, 5, 5.7, 'JAPAN:  HONSHU:  S. OF', 31.529, 140.213, 0, 0, 0, 0), (2015, 5, 7.3, 'NEPAL:   DOLAKHA', 27.809, 86.066, 117, 0, 2800, 0), (2015, 5, 7.5, 'PAPUA NEW GUINEA', -5.462, 151.875, 0, 0, 0, 0), (2015, 5, 7.8, 'JAPAN:  BONIN ISLANDS [CHICHIJIMA ISLAND]', 27.839, 140.493, 0, 0, 12, 0), (2015, 6, 5.3, 'INDIA:  KOKRAJHAR', 26.638, 90.41, 0, 0, 2, 0), (2015, 7, 5.1, 'PAKISTAN:  ABBOTTABAD', 33.856, 73.193, 3, 0, 1, 0), (2015, 7, 5.9, 'COLOMBIA-PANAMA:  COLOMBIA:  UNGUIA', 8.231, -77.315, 0, 0, 6, 0), (2015, 7, 6.1, 'PHILIPPINES:  MINDANAO', 10.169, 125.891, 1, 0, 0, 0), (2015, 7, 6.4, 'CHINA:  S. XINJIANG:  HOTAN', 37.6, 78.2, 3, 0, 263, 0), (2015, 7, 6.7, 'SOLOMON ISLANDS', -9.307, 158.403, 0, 0, 0, 0), (2015, 7, 6.9, 'USA: ALASKA', 52.214, -169.399, 0, 0, 0, 0), (2015, 7, 7.0, 'INDONESIA:  PAPUA', -2.629, 138.528, 1, 0, 0, 0), (2015, 7, 7.0, 'SOLOMON ISLANDS', -10.401, 165.141, 0, 0, 0, 0), (2015, 8, 4.5, 'EL SALVADOR:  ALEGRIA', 13.668, -88.478, 0, 0, 4, 0), (2015, 8, 5.8, 'RWANDA:  BUKAVU', -2.141, 28.897, 3, 0, 30, 0), (2015, 9, 6.6, 'INDONESIA:  SORONG', -0.59, 131.27, 0, 0, 62, 0), (2015, 9, 8.3, 'CHILE:  CENTRAL', -31.573, -71.674, 7, 1, 14, 600.0), (2015, 10, 5.8, 'ARGENTINA:  GALPON', -25.442, -64.632, 2, 0, 30, 0), (2015, 10, 7.5, 'AFGHANISTAN: HINDU KUSH', 36.524, 70.368, 399, 0, 1770, 109.0), (2015, 11, 5.1, 'VENEZUELA:  MERIDA', 8.48, -71.42, 1, 0, 3, 0), (2015, 11, 5.3, 'VENEZUELA:  MERIDA', 8.477, -71.365, 1, 0, 0, 0), (2015, 11, 5.6, 'KYRGYZSTAN: OSH', 40.376, 73.204, 0, 0, 0, 0), (2015, 11, 6.5, 'INDONESIA:  EAST NUSA TENGGARA:  ALOR', -8.338, 124.875, 0, 0, 0, 9.0), (2015, 11, 6.7, 'JAPAN:  KYUSYU ISLAND', 31.001, 128.873, 0, 0, 0, 0), (2015, 11, 6.8, 'SOLOMON ISLANDS', -8.899, 158.422, 0, 0, 0, 0), (2015, 11, 6.9, 'CHILE:  LA SERENA', -29.439, -72.105, 0, 0, 0, 0), (2015, 11, 7.6, 'PERU-BRAZIL', -10.77, -71.41, 0, 0, 0, 0), (2015, 11, 7.6, 'PERU-BRAZIL', -10.07, -70.98, 0, 0, 0, 0), (2015, 12, 6.3, 'AFGHANISTAN; PAKISTAN', 36.494, 71.126, 4, 0, 97, 0), (2015, 12, 6.6, 'MEXICO:  COCOTITLAN', 15.802, -93.633, 2, 0, 0, 0), (2015, 12, 7.2, 'TAJIKISTAN', 38.211, 72.78, 2, 0, 0, 5.0), (2016, 1, 6.3, 'MOROCCO:  MELILLA', 35.649, -3.682, 1, 0, 26, 0), (2016, 1, 6.7, 'INDIA:  IMPAHL', 24.804, 93.651, 13, 0, 100, 75.0), (2016, 1, 7.1, 'USA: ALASKA:  KENAI', 59.658, -153.452, 0, 0, 0, 0), (2016, 2, 6.4, 'TAIWAN:  TAINAN', 22.97, 120.46, 117, 0, 525, 700.0), (2016, 3, 7.8, 'INDONESIA: SUMATRA:', -4.952, 94.33, 0, 0, 0, 0), (2016, 4, 6.6, 'AFGHANISTAN:  KHYBER PAKHTUNKHWA', 36.473, 71.131, 6, 0, 5, 0), (2016, 4, 6.9, 'INDIA: ASSAM; BANGLADESH', 23.094, 94.865, 2, 0, 170, 0), (2016, 4, 7.0, 'VANUATU ISLANDS', -16.043, 167.379, 0, 0, 0, 0), (2016, 5, 5.2, 'CHINA:  TIBET (XIZANG PROVINCE)', 32.022, 95.027, 0, 0, 60, 0), (2016, 5, 5.4, 'ALGERIA:  MEDEA:  MIHOUB', 36.431, 3.517, 0, 0, 28, 0), (2016, 5, 6.9, 'ECUADOR:  MANABI PROVINCE', 0.495, -79.616, 1, 0, 162, 0), (2016, 6, 6.3, 'INDONESIA:  MALUKU:  TERNATE ISLAND', 1.279, 126.371, 0, 0, 0, 0), (2016, 6, 6.6, 'INDONESIA:  SUMATRA:  PESISIR SELATAN', -2.097, 100.665, 1, 0, 30, 0), (2016, 7, 4.9, 'CHINA:  GUANGXI PROVINCE', 24.134, 111.478, 0, 0, 0, 0), (2016, 7, 5.0, 'TAJIKISTAN:  RASHT', 38.881, 70.559, 0, 0, 0, 0), (2016, 7, 5.6, 'INDONESIA:  SUMBAWA ISLAND:  WEST NUSA TENGGARA', -8.194, 117.814, 0, 0, 4, 0), (2016, 7, 7.7, 'NORTHERN MARIANA ISLANDS', 18.543, 145.507, 0, 0, 0, 0), (2016, 8, 5.5, 'PERU:  AREQUIPA', -15.64, -71.68, 9, 0, 68, 0), (2016, 8, 6.0, 'JAPAN:  OFF EAST COAST HONSHU', 40.394, 143.68, 0, 0, 0, 0), (2016, 8, 6.8, 'MYANMAR (BURMA): CHAUK', 20.923, 94.569, 4, 0, 20, 10.0), (2016, 8, 7.2, 'NEW CALEDONIA:  LOYALTY ISLANDS', -22.477, 173.117, 0, 0, 0, 0), (2016, 8, 7.4, 'SOUTH SANDWICH ISLANDS', -55.285, -31.877, 0, 0, 0, 0), (2016, 9, 4.8, 'RWANDA:  RISUZI; CONGO:  UKAVU', -2.65, 29.06, 8, 0, 0, 0), (2016, 9, 5.1, 'BALKANS NW:  MACEDONIA', 42.008, 21.488, 0, 0, 30, 10.0), (2016, 9, 5.4, 'SOUTH KOREA:  GYEONGJU', 35.781, 129.216, 1, 0, 14, 21.0), (2016, 9, 5.5, 'NICARAGUA:  LEON', 12.442, -86.515, 1, 0, 5, 0), (2016, 9, 5.9, 'TANZANIA:  LAKE VICTORIA;  UGANDA: RAKAI', -1.036, 31.618, 23, 0, 252, 458.0), (2016, 9, 7.0, 'NEW ZEALAND:  GISBORNE', -37.359, 179.146, 0, 0, 0, 0), (2016, 10, 6.2, 'JAPAN:  KURAYOSHI', 35.374, 133.809, 0, 0, 7, 100.0), (2016, 10, 6.6, 'ITALY: NORCIA', 42.84, 13.11, 2, 0, 20, 200.0), (2016, 11, 4.2, 'POLAND:  RUDNA', 51.613, 16.157, 8, 0, 9, 0), (2016, 11, 5.0, 'USA: OKLAHOMA:  CUSHING', 35.988, -96.805, 0, 0, 0, 20.0), (2016, 11, 6.6, 'CHINA:  XINJIANG PROVINCE:  KASHGAR', 39.273, 73.978, 1, 0, 0, 5.5), (2016, 11, 6.9, 'JAPAN: NEAR E COAST HONSHU', 37.393, 141.387, 0, 0, 15, 0), (2016, 11, 6.9, 'NICARAGUA', 11.96, -88.835, 0, 0, 0, 0), (2016, 11, 7.8, 'NEW ZEALAND:  AMBERLEY', -42.737, 173.054, 2, 0, 0, 0), (2016, 12, 5.4, 'ECUADOR:  ESMERALDAS', 0.93, -79.84, 3, 0, 47, 0), (2016, 12, 6.0, 'CHINA:  N. XINJIANG:  URUMQI', 43.823, 86.345, 1, 0, 0, 135.0), (2016, 12, 6.5, 'INDONESIA:  SUMATRA:  ACEH:  PIDIE JAYA', 5.283, 96.168, 104, 0, 857, 100.0), (2016, 12, 6.9, 'SOLOMON ISLANDS', -10.749, 161.132, 0, 0, 0, 0), (2016, 12, 7.6, 'CHILE', -43.517, -74.391, 0, 0, 0, 0), (2016, 12, 7.8, 'SOLOMON ISLANDS', -10.681, 161.327, 1, 0, 0, 0), (2016, 12, 7.9, 'PAPUA NEW GUINEA:  NEW BRITAIN NEW IRELAND', -4.505, 153.522, 0, 0, 0, 0), (2017, 1, 5.0, 'IRAN:  KHONJ', 28.2, 53.107, 4, 0, 4, 0), (2017, 1, 5.5, 'MADAGASCAR: ANTSIRABE', -20.16, 46.647, 2, 0, 0, 0), (2017, 1, 5.7, 'INDIA:  AMBASA;  BANGLADESH', 24.015, 92.018, 3, 0, 0, 0), (2017, 1, 5.7, 'ITALY:  FARINDOLA', 42.529, 13.282, 34, 0, 11, 18.0), (2017, 1, 6.9, 'FIJI ISLANDS', -19.373, 176.052, 0, 0, 0, 0), (2017, 1, 7.9, 'PAPUA NEW GUINEA:  BOUGAINVILLE ISLAND', -6.246, 155.172, 3, 0, 0, 0), (2017, 2, 5.3, 'TURKEY:  CANAKKALE', 39.599, 26.065, 0, 0, 5, 0), (2017, 2, 5.5, 'COLOMBIA:  HUILA', 3.449, -74.672, 0, 0, 0, 0), (2017, 2, 5.9, 'ZAMBIA:  KAPUTA', -8.44, 30.031, 0, 0, 5, 0), (2017, 2, 6.3, 'PAKISTAN:  PASNI', 25.191, 63.264, 0, 0, 0, 0), (2017, 2, 6.5, 'PHILIPPINES: SURIGAO DEL NORTE', 9.907, 125.452, 8, 0, 202, 40.0), (2017, 3, 5.0, 'CHINA:   YUNNAN PROVINCE', 25.938, 99.841, 0, 0, 1, 31.0), (2017, 3, 5.1, 'MYANMAR (BURMA):  THARRAWADDY', 17.399, 96.0, 2, 0, 36, 0), (2017, 3, 5.6, 'INDONESIA:  BALI', -8.492, 115.323, 0, 0, 4, 0), (2017, 3, 5.7, 'PHILIPPINES: SURIGAO DEL NORTE', 9.831, 125.496, 1, 0, 45, 0), (2017, 4, 6.1, 'IRAN:  SEFID SANG', 35.776, 60.436, 2, 0, 11, 0), (2017, 4, 6.9, 'CHILE:  VALPARAISO', -33.038, -72.062, 0, 0, 0, 0), (2017, 4, 6.9, 'PHILIPPINES: SARANGANI', 5.504, 125.066, 0, 0, 5, 0), (2017, 5, 4.4, 'TANZANIA: MWANZA', -3.043, 32.888, 1, 0, 18, 0), (2017, 5, 5.1, 'IRAN:  ARDABIL', 39.816, 48.57, 0, 0, 20, 0), (2017, 5, 5.6, 'IRAN: KHORASAN', 37.769, 57.206, 3, 0, 417, 2.0), (2017, 5, 6.2, 'ALASKA:  SKAGWAY; CANADA:  BRITISH COLUMBIA', 59.852, -136.677, 0, 0, 0, 0), (2017, 5, 6.6, 'INDONESIA:  SULAWESI:  POSO', -1.292, 120.431, 0, 0, 25, 0), (2017, 6, 3.2, 'NEPAL:  DHADING', 27.64, 85.17, 1, 0, 1, 0), (2017, 6, 5.6, 'MOZAMBIQUE', -19.45, 34.488, 0, 0, 4, 0), (2017, 6, 6.3, 'GREECE: LESBOS', 38.93, 26.365, 1, 0, 15, 0), (2017, 7, 6.4, 'PERU:  AREQUIPA', -16.416, -73.636, 1, 0, 1, 0), (2017, 7, 6.5, 'PHILIPPINES: LEYTE', 11.127, 124.629, 4, 0, 448, 5.0), (2017, 7, 7.7, 'RUSSIA: BERING ISLAND', 54.443, 168.857, 0, 0, 0, 0), (2017, 8, 4.2, 'ITALY:  ISCHIA ISLAND', 40.783, 13.939, 2, 0, 42, 0), (2017, 8, 5.0, 'PHILIPPINES: LEYTE: ORMOC', 10.954, 124.707, 2, 0, 0, 0), (2017, 8, 5.4, 'CHILE:  SANTIAGO', -33.201, -70.614, 1, 0, 0, 0), (2017, 8, 5.6, 'PERU: AREQUIPA', -16.299, -73.474, 1, 0, 0, 0), (2017, 8, 5.8, 'PERU:  JUNIN', -10.721, -74.566, 1, 0, 2, 0), (2017, 8, 6.3, 'CHINA:  XINGJIANG: BORTALA', 44.302, 82.832, 0, 0, 32, 0), (2017, 8, 6.5, 'CHINA:  SICHUAN PROVINCE:  ABA', 33.193, 103.855, 29, 0, 525, 500.0), (2017, 9, 5.7, 'PHILIPPINES: MINDANAO: LANAO DEL SUR PROVINCE', 7.562, 124.743, 0, 0, 11, 0), (2017, 9, 6.1, 'MEXICO:  OAXACA', 16.626, -95.078, 5, 0, 7, 0), (2017, 10, 6.1, 'INDONESIA:  MALUKU:  AMBON', -3.745, 127.752, 1, 0, 0, 0), (2017, 10, 6.7, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.697, 169.149, 0, 0, 0, 0), (2017, 11, 5.1, 'CHINA: CHONGQING: WULONG', 29.349, 108.058, 0, 0, 8, 1.5), (2017, 11, 5.5, 'SOUTH KOREA: POHANG', 36.074, 129.27, 0, 0, 90, 52.0), (2017, 11, 5.8, 'INDONESIA: NORTH MALUKU: MOROTAI', 2.465, 128.148, 1, 0, 0, 0), (2017, 11, 6.3, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.638, 168.673, 0, 0, 0, 0), (2017, 11, 6.4, 'CHINA:  TIBET (XIZANG PROVINCE): NYINGCHI', 29.833, 94.984, 0, 0, 3, 0), (2017, 11, 6.5, 'COSTA RICA: JACO', 9.515, -84.487, 2, 0, 0, 0), (2017, 11, 6.6, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.648, 168.859, 0, 0, 0, 0), (2017, 11, 6.6, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.503, 168.598, 0, 0, 0, 0), (2017, 11, 7.0, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.325, 168.672, 0, 0, 0, 0), (2017, 11, 7.3, 'IRAN: KERMANSHAH; IRAQ: KURDISTAN', 34.911, 45.959, 630, 0, 12900, 750.0), (2017, 12, 4.9, 'IRAN:  ALBORZ', 35.649, 50.962, 2, 0, 117, 0), (2017, 12, 6.1, 'IRAN:  KERMAN', 30.746, 57.307, 0, 0, 51, 0), (2017, 12, 6.5, 'INDONESIA:  JAVA', -7.492, 108.174, 4, 0, 36, 0), (2018, 1, 3.4, 'THE NETHERLANDS: GRONINGEN', 53.2, 6.6, 0, 0, 0, 0), (2018, 1, 4.9, 'BALKANS NW:  MONTENEGRO: BERANE', 42.658, 19.883, 0, 0, 0, 0), (2018, 1, 5.0, 'IRAN:  KERMANSHAH', 34.649, 45.799, 0, 0, 51, 0), (2018, 1, 5.2, 'ECUADOR:  PASTAZA', -1.756, -77.694, 1, 0, 0, 0), (2018, 1, 5.5, 'IRAN: KERMANSHAH', 33.764, 45.749, 0, 0, 13, 0), (2018, 1, 6.0, 'INDONESIA:  JAVA:  BANTEN', -7.196, 105.918, 1, 0, 11, 0), (2018, 1, 6.1, 'AFGHANISTAN; PAKISTAN:  BALUCHISTAN', 36.543, 70.816, 2, 0, 15, 0), (2018, 1, 7.1, 'PERU: YAUCA', -15.776, -74.744, 2, 0, 139, 0), (2018, 1, 7.5, 'HONDURAS', 17.474, -83.519, 0, 0, 0, 0), (2018, 1, 7.9, 'USA: ALASKA:  KODIAK ISLAND', 56.046, -149.073, 0, 0, 0, 0), (2018, 2, 6.1, 'PAPUA NEW GUINEA:  S HIGHLANDS', -6.182, 142.492, 1, 0, 0, 0), (2018, 2, 6.4, 'TAIWAN:  HUALIEN', 24.174, 121.653, 17, 0, 291, 0), (2018, 2, 7.2, 'MEXICO:  OAXACA', 16.646, -97.653, 13, 0, 0, 0), (2018, 3, 6.0, 'PAPUA NEW GUINEA:  S HIGHLANDS', -6.307, 142.62, 11, 0, 0, 0), (2018, 4, 4.4, 'INDONESIA:  JAVA:  BANJARNEGARA', -7.21, 109.65, 3, 0, 21, 0), (2018, 4, 4.7, 'ITALY:  MUCCIA', 43.093, 13.046, 0, 0, 0, 0), (2018, 4, 4.9, 'VENEZUELA:  MERIDA', 8.346, -71.664, 0, 0, 0, 0), (2018, 4, 5.2, 'TURKEY:  ADIYAMAN', 37.596, 38.514, 0, 0, 39, 0), (2018, 4, 5.3, 'IRAN:  KERMANSHAH', 34.456, 45.764, 0, 0, 54, 0), (2018, 4, 5.6, 'JAPAN:  SHIMANE PREFECTURE', 35.262, 132.541, 0, 0, 8, 0), (2018, 4, 6.3, 'PAPUA NEW GUINEA:  HELA', -5.841, 142.49, 4, 0, 0, 0), (2018, 5, 2.1, 'SOUTH AFRICA:  WEST RAND', -26.4, 27.5, 7, 0, 6, 0), (2018, 5, 4.1, 'POLAND:  SILESIAN:  JASTRZEBIE-ZDROJ', 50.11, 18.71, 5, 0, 2, 0), (2018, 5, 5.1, 'CHINA:  JILIN PROVINCE:  NINGJIANG', 45.279, 124.557, 0, 0, 0, 0), (2018, 5, 5.3, 'IRAN:  KOHGILUYEH AND BOYER-AHMAD: SISAKHT', 30.715, 51.485, 0, 0, 133, 0), (2018, 5, 5.8, 'COMOROS:  MAYOTTE', -12.778, 45.593, 0, 0, 3, 0), (2018, 5, 6.2, 'AFGHANISTAN: TAKHAR;  PAKISTAN', 36.99, 71.369, 0, 0, 13, 0), (2018, 5, 6.9, 'USA: HAWAIIAN ISLANDS: PUNA DISTRICT', 19.37, -155.032, 0, 0, 0, 0), (2018, 6, 4.9, 'COLOMBIA:  PASTO', 1.032, -77.259, 2, 0, 0, 0), (2018, 6, 5.3, 'AZERBAIJAN: SHAKI-ZAQATALA', 41.526, 46.785, 1, 0, 31, 0), (2018, 6, 5.5, 'JAPAN:  OSAKA', 34.833, 135.612, 5, 0, 380, 7000.0), (2018, 7, 5.2, 'INDONESIA: SUMATRA: SOLOK', -0.965, 100.771, 1, 0, 2, 0), (2018, 7, 5.9, 'IRAN:  KERMANSHAH', 34.645, 46.179, 0, 0, 287, 0), (2018, 7, 6.4, 'INDONESIA:  LOMBOK ISLAND', -8.274, 116.491, 17, 0, 355, 0), (2018, 8, 5.0, 'CHINA:   YUNNAN PROVINCE:  YUXI', 24.322, 102.941, 0, 0, 24, 0), (2018, 8, 5.9, 'INDONESIA:  LOMBOK ISLAND', -8.394, 116.208, 2, 0, 24, 0), (2018, 8, 6.0, 'IRAN:  KERMANSHAH', 34.663, 46.277, 2, 0, 267, 0), (2018, 8, 6.3, 'INDONESIA:  LOMBOK ISLAND', -8.325, 116.577, 2, 0, 1, 0), (2018, 8, 6.9, 'INDONESIA:  LOMBOK ISLAND', -8.324, 116.626, 10, 0, 24, 0), (2018, 8, 6.9, 'INDONESIA:  LOMBOK ISLAND', -8.287, 116.452, 560, 0, 7733, 509.0), (2018, 8, 7.1, 'NEW CALEDONIA:  LOYALTY ISLANDS', -22.066, 170.05, 0, 0, 0, 0), (2018, 8, 7.3, 'VENEZUELA:  SUCRE; TRINIDAD', 10.855, -62.883, 5, 0, 0, 0), (2018, 8, 8.2, 'FIJI ISLANDS', -18.178, -178.111, 0, 0, 0, 0), (2018, 9, 5.3, 'INDIA:  WEST BENGAL', 26.374, 90.165, 1, 0, 0, 0), (2018, 9, 5.5, 'IRAN:  KERMAN', 28.342, 59.315, 1, 0, 2, 0), (2018, 9, 5.6, 'CHINA: YUNNAN PROVINCE:  MOJIANG HANI', 23.332, 101.552, 0, 0, 28, 0), (2018, 9, 6.6, 'JAPAN:  HOKKAIDO', 42.671, 141.933, 44, 0, 660, 2000.0), (2018, 9, 7.5, 'INDONESIA:  SULAWESI', -0.178, 119.84, 4340, 667, 10679, 1500.0), (2018, 9, 7.8, 'FIJI ISLANDS', -18.494, 179.332, 0, 0, 0, 0), (2018, 10, 5.9, 'HAITI: PORT-DEX-PAIX', 20.041, -72.975, 18, 0, 580, 0), (2018, 10, 6.5, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.743, 169.522, 0, 0, 0, 0), (2018, 11, 4.9, 'AFGHANISTAN:  HINDU KUSH:  BAGHLAN', 35.817, 68.682, 0, 0, 9, 0), (2018, 11, 5.6, 'INDONESIA:  SULAWESI:  MAMASA', -2.916, 119.435, 7, 0, 0, 0), (2018, 11, 6.3, 'IRAN: KERMANSHAH; IRAQ: KURDISTAN', 34.304, 45.74, 1, 0, 759, 0), (2018, 11, 7.0, 'USA: ALASKA:  ANCHORAGE', 61.34, -149.937, 0, 0, 117, 150.0), (2018, 12, 5.1, 'ITALY:  SICILY:  CATANIA', 37.555, 15.166, 0, 0, 28, 115.0), (2018, 12, 5.4, 'CHINA:  SICHUAN:  YIBIN', 28.264, 104.991, 0, 0, 17, 7.255), (2018, 12, 5.5, 'MOZAMBIQUE', -20.644, 32.801, 0, 0, 10, 0), (2018, 12, 5.6, 'VANUATU ISLANDS: AMBRYM ISLAND', -16.368, 168.213, 0, 0, 0, 0), (2018, 12, 7.5, 'NEW CALEDONIA:  LOYALTY ISLANDS', -21.969, 169.446, 0, 0, 0, 0), (2019, 1, 3.4, 'POLAND:  RYDULTOWY', 50.08, 18.39, 1, 0, 8, 0), (2019, 1, 3.8, 'POLAND:  RUDNA', 51.52, 16.09, 1, 0, 6, 0), (2019, 1, 5.2, 'CHINA:  SICHUAN:  YIBIN', 28.261, 104.984, 0, 0, 774, 0), (2019, 1, 5.6, 'IRAN:  KERMANSHAH: SARPOL-E ZAHAB', 34.121, 45.681, 0, 0, 75, 0), (2019, 2, 3.6, 'INDIA:  MAHARASHTRA:  PALGHAR', 19.9, 72.8, 1, 0, 0, 0), (2019, 2, 4.9, 'CHINA:  SICHUAN PROVINCE: RONGXIAN', 29.498, 104.632, 2, 0, 12, 2.0), (2019, 2, 5.1, 'AZERBAIJAN:  SHEMAKHA (SEMACHA)', 40.892, 48.602, 0, 0, 3, 0), (2019, 2, 5.4, 'INDONESIA: SUMATRA: SOLOK', -1.301, 101.601, 0, 0, 48, 0), (2019, 2, 6.6, 'MEXICO:  CHIAPAS; GUATEMALA:  SAN MARCOS', 14.763, -92.298, 0, 0, 4, 0), (2019, 3, 5.5, 'INDONESIA:  LOMBOK ISLAND', -8.418, 116.52, 6, 0, 0, 0), (2019, 3, 7.0, 'PERU:  AREQUIPA', -14.684, -70.127, 1, 0, 1, 0), (2019, 4, 6.1, 'PHILIPPINES:  PAMPANGA PROVINCE', 14.924, 120.497, 18, 3, 183, 50.0), (2019, 4, 6.1, 'TAIWAN:  HUALIEN', 23.989, 121.693, 1, 0, 16, 0), (2019, 4, 6.8, 'INDONESIA:  SULAWESI ISLAND: LUWUK', -1.852, 122.553, 1, 0, 0, 0), (2019, 5, 3.2, 'THE NETHERLANDS: GRONINGEN', 53.394, 6.586, 0, 0, 0, 0), (2019, 5, 4.8, 'CHINA:  JILIN PROVINCE:  SONGYUAN', 45.205, 124.611, 0, 0, 0, 0), (2019, 5, 6.6, 'EL SALVADOR:  SAN SALVADOR', 13.199, -89.306, 1, 0, 1, 0), (2019, 5, 7.2, 'PAPUA NEW GUINEA:  MOROBE: WAMPAR', -6.977, 146.44, 0, 0, 0, 0), (2019, 6, 5.2, 'ALBANIA:  KORCE', 40.501, 20.722, 0, 0, 4, 0), (2019, 6, 5.8, 'CHINA:  SICHUAN:  YIBIN', 28.405, 104.957, 13, 0, 200, 1300.0), (2019, 6, 6.4, 'CHILE:  COQUIMBO', -30.056, -72.082, 0, 0, 0, 0), (2019, 6, 6.4, 'JAPAN:  NIIGATA PREFECTURE', 38.646, 139.472, 0, 0, 28, 0), (2019, 7, 3.1, 'POLAND:  KATOWICE', 50.287, 18.997, 3, 0, 6, 0), (2019, 7, 3.8, 'INDIA:  MAHARASHTRA:  PALGHAR', 20.0, 72.9, 1, 0, 0, 0), (2019, 7, 5.3, 'GREECE:  ATHENS', 38.115, 23.505, 0, 0, 4, 0), (2019, 7, 5.7, 'IRAN:  MASJED-E SOLEYMAN', 31.775, 49.542, 1, 0, 128, 0), (2019, 7, 5.8, 'PHILIPPINES: MINDANAO: SURIGAO DEL SUR PROVINCE', 9.334, 126.04, 0, 0, 59, 0.71), (2019, 7, 6.0, 'PHILIPPINES:  BATANES:  ITBAYAT', 20.807, 121.986, 9, 0, 64, 0.925), (2019, 7, 6.4, 'USA: CALIFORNIA:  RIDGECREST;  NEVADA', 35.705, -117.506, 1, 0, 0, 0), (2019, 7, 7.1, 'USA: CALIFORNIA:  RIDGECREST', 35.766, -117.605, 0, 0, 0, 5300.0), (2019, 7, 7.3, 'INDONESIA:  MOLUCCA ISLANDS:  N', -0.529, 128.093, 8, 0, 134, 0), (2019, 8, 5.8, 'TURKEY:  DENIZLI', 37.948, 29.697, 0, 0, 0, 0), (2019, 8, 5.9, 'TAIWAN:  TAIPEI', 24.475, 121.947, 1, 0, 0, 0), (2019, 8, 6.9, 'INDONESIA:  JAVA:  BANTEN', -7.267, 104.825, 6, 0, 3, 0), (2019, 9, 5.1, 'CHINA:  SICHUAN PROVINCE: NEIJIANG', 29.573, 105.064, 1, 0, 63, 0), (2019, 9, 5.6, 'ALBANIA:  DURRES', 41.381, 19.454, 0, 0, 132, 45.0), (2019, 9, 5.6, 'PAKISTAN:  MIRPUR DISTRICT', 33.106, 73.766, 39, 0, 746, 17.0), (2019, 9, 5.7, 'TURKEY:  ISTANBUL', 40.89, 28.173, 1, 0, 34, 0), (2019, 9, 6.1, 'CHILE:  SOUTH CENTRAL', -40.815, -72.002, 1, 0, 0, 0), (2019, 9, 6.5, 'INDONESIA:  MALUKU:  AMBON', -3.45, 128.347, 31, 0, 179, 0), (2019, 9, 6.8, 'CHILE:  CONCEPCION', -35.473, -73.162, 1, 0, 0, 0), (2019, 10, 5.0, 'INDONESIA:  PASSO', -3.65, 128.216, 1, 0, 2, 0), (2019, 11, 5.0, 'CHINA:  GUANGXI PROVINCE', 22.96, 106.711, 1, 0, 4, 0), (2019, 11, 5.0, 'INDONESIA:  MALUKU:  AMBON', -3.61, 128.299, 2, 0, 3, 0), (2019, 11, 5.9, 'PHILIPPINES:  MINDANAO:  BUKIDNON PROVINCE', 7.625, 124.912, 0, 0, 16, 0), (2019, 11, 7.1, 'INDONESIA:  MOLUCCA ISLANDS:  N', 1.6, 126.416, 1, 0, 3, 0), (2019, 12, 5.2, 'CHINA:  SICHUAN PROVINCE: NEIJIANG', 29.639, 104.946, 0, 0, 18, 0), (2019, 12, 6.8, 'PHILIPPINES:  MINDANAO:  DAVAO', 6.708, 125.188, 13, 1, 210, 0), (2020, 1, 6.0, 'CHINA:  XINJIANG PROVINCE', 39.831, 77.106, 1, 0, 2, 0), (2020, 1, 6.7, 'TURKEY:  ELAZIG AND MALATYA PROVINCES', 38.39, 39.081, 41, 0, 1600, 0), (2020, 1, 7.7, 'CUBA: GRANMA;  CAYMAN IS;  JAMAICA', 19.44, -78.755, 0, 0, 0, 0), (2020, 2, 6.0, 'TURKEY: VAN;  IRAN', 38.482, 44.367, 10, 0, 60, 0), (2020, 3, 5.4, 'BALKANS NW:  CROATIA:  ZAGREB', 45.897, 15.966, 1, 0, 27, 6000.0), (2020, 3, 5.7, 'USA: UTAH', 40.751, -112.078, 0, 0, 0, 48.5), (2020, 3, 7.5, 'RUSSIA:  KURIL ISLANDS', 48.986, 157.693, 0, 0, 0, 0), (2020, 4, 5.3, 'CHINA:  QINGHAI PROVINCE', 33.124, 98.916, 0, 0, 0, 11.28), (2020, 5, 5.2, 'CHINA:   YUNNAN PROVINCE:  QIAOJIA', 27.296, 103.281, 4, 0, 24, 0), (2020, 5, 6.6, 'GREECE:  CRETE', 34.205, 25.712, 0, 0, 0, 0), (2020, 6, 4.5, 'PERU:  COAST:  CHIMBOTE', -9.634, -78.591, 1, 0, 0, 0), (2020, 6, 5.4, 'TURKEY:  VAN', 38.558, 44.023, 0, 0, 5, 0), (2020, 6, 5.9, 'TURKEY:  BINGOL', 39.421, 40.697, 1, 0, 17, 0), (2020, 6, 6.4, 'INDONESIA: NORTH MALUKU: MOROTAI', 2.923, 128.248, 0, 0, 0, 0), (2020, 6, 7.4, 'MEXICO: OAXACA', 16.029, -95.901, 10, 0, 0, 0), (2020, 7, 4.8, 'VIETNAM: SON LA PROVINCE', 20.872, 104.541, 0, 0, 0, 0), (2020, 7, 7.8, 'USA: ALASKA', 55.03, -158.522, 0, 0, 0, 0), (2020, 8, 5.1, 'USA: NORTH CAROLINA:  SPARTA', 36.476, -81.094, 0, 0, 0, 0), (2020, 8, 6.6, 'PHILIPPINES:  MASBATE', 12.021, 124.123, 1, 0, 48, 0)]
year_range = (2015,2020)
student = summary_statistics(data,*year_range)
instructor = [[(2015, 44), (2016, 43), (2017, 53), (2018, 60), (2019, 48), (2020, 19)], [(2015, 10737.65), (2016, 1834.5), (2017, 1399.5), (2018, 11281.255), (2019, 6715.635), (2020, 6059.78)], [(2015, (8753, 367, 22991)), (2016, (309, 0, 2454)), (2017, (751, 0, 15102)), (2018, (5086, 667, 22816)), (2019, (168, 4, 3171)), (2020, (70, 0, 1783))]]
print("instructor:\n", *instructor, sep='\n')
print("student:\n", *student, sep='\n')
for i, val in enumerate(instructor):
    if student[i] != instructor[i]:
        print(i)
        print("instructor:\n", instructor[i])
        print("student:\n", student[i])
assert student == instructor
print("Year range:", *year_range)
print("\nStudent quakes_year:", student[0])
print("Instructor quakes_year:",instructor[0])
assert student[0] == instructor[0]
print("\nStudent cost_year:", student[1])
print("Instructor cost_year:",instructor[1])
assert student[1] == instructor[1]
print("\nStudent casualty_year:", student[2])
print("Instructor casualty_year:",instructor[2])
assert student[2] == instructor[2]
###################################################################
year_range = (2001,2020)
student = summary_statistics(data, *year_range)
instructor = [[(2001, 0), (2002, 0), (2003, 0), (2004, 0), (2005, 0), (2006, 0), (2007, 0), (2008, 0), (2009, 0), (2010, 0), (2011, 0), (2012, 0), (2013, 0), (2014, 0), (2015, 44), (2016, 43), (2017, 53), (2018, 60), (2019, 48), (2020, 19)], [(2001, 0), (2002, 0), (2003, 0), (2004, 0), (2005, 0), (2006, 0), (2007, 0), (2008, 0), (2009, 0), (2010, 0), (2011, 0), (2012, 0), (2013, 0), (2014, 0), (2015, 10737.65), (2016, 1834.5), (2017, 1399.5), (2018, 11281.255), (2019, 6715.635), (2020, 6059.78)], [(2001, (0, 0, 0)), (2002, (0, 0, 0)), (2003, (0, 0, 0)), (2004, (0, 0, 0)), (2005, (0, 0, 0)), (2006, (0, 0, 0)), (2007, (0, 0, 0)), (2008, (0, 0, 0)), (2009, (0, 0, 0)), (2010, (0, 0, 0)), (2011, (0, 0, 0)), (2012, (0, 0, 0)), (2013, (0, 0, 0)), (2014, (0, 0, 0)), (2015, (8753, 367, 22991)), (2016, (309, 0, 2454)), (2017, (751, 0, 15102)), (2018, (5086, 667, 22816)), (2019, (168, 4, 3171)), (2020, (70, 0, 1783))]]
print("student:\n", *student, sep='\n')
print("instructor:\n", *instructor, sep='\n')
assert student == instructor
assert student == instructor
print("Year range:", *year_range)
print("\nStudent quakes_year:", student[0])
print("Instructor quakes_year:",instructor[0])
assert student[0] == instructor[0]
print("\nStudent cost_year:", student[1])
print("Instructor cost_year:",instructor[1])
assert student[1] == instructor[1]
print("\nStudent damage_year:", student[2])
print("Instructor damage_year:",instructor[2])
assert student[2] == instructor[2]
###################################################################
year_range = (2020,2020)
student = summary_statistics(data,*year_range)
instructor = [[(2020, 19)], [(2020, 6059.78)], [(2020, (70, 0, 1783))]]
print("student:\n",student)
print("instructor:\n",instructor)
assert student == instructor
print("Year range:", *year_range)
print("\nStudent quakes_year:", student[0])
print("Instructor quakes_year:",instructor[0])
assert student[0] == instructor[0]
print("\nStudent cost_year:", student[1])
print("Instructor cost_year:",instructor[1])
assert student[1] == instructor[1]
print("\nStudent damage_year:", student[2])
print("Instructor damage_year:",instructor[2])
assert student[2] == instructor[2]