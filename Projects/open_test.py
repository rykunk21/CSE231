import csv
Instructor = [(2020, 1, 6.0, 'CHINA:  XINJIANG PROVINCE', 39.831, 77.106, 1, 0, 2, 0), (2020, 1, 6.7, 'TURKEY:  ELAZIG AND MALATYA PROVINCES', 38.39, 39.081, 41, 0, 1600, 0), (2020, 1, 7.7, 'CUBA: GRANMA;  CAYMAN IS;  JAMAICA', 19.44, -78.755, 0, 0, 0, 0), (2020, 2, 6.0, 'TURKEY: VAN;  IRAN', 38.482, 44.367, 10, 0, 60, 0), (2020, 3, 5.4, 'BALKANS NW:  CROATIA:  ZAGREB', 45.897, 15.966, 1, 0, 27, 6000.0), (2020, 3, 5.7, 'USA: UTAH', 40.751, -112.078, 0, 0, 0, 48.5), (2020, 3, 7.5, 'RUSSIA:  KURIL ISLANDS', 48.986, 157.693, 0, 0, 0, 0), (2020, 4, 5.3, 'CHINA:  QINGHAI PROVINCE', 33.124, 98.916, 0, 0, 0, 11.28), (2020, 5, 5.2, 'CHINA:   YUNNAN PROVINCE:  QIAOJIA', 27.296, 103.281, 4, 0, 24, 0), (2020, 5, 6.6, 'GREECE:  CRETE', 34.205, 25.712, 0, 0, 0, 0), (2020, 6, 4.5, 'PERU:  COAST:  CHIMBOTE', -9.634, -78.591, 1, 0, 0, 0), (2020, 6, 5.4, 'TURKEY:  VAN', 38.558, 44.023, 0, 0, 5, 0), (2020, 6, 5.9, 'TURKEY:  BINGOL', 39.421, 40.697, 1, 0, 17, 0), (2020, 6, 6.4, 'INDONESIA: NORTH MALUKU: MOROTAI', 2.923, 128.248, 0, 0, 0, 0), (2020, 6, 7.4, 'MEXICO: OAXACA', 16.029, -95.901, 10, 0, 0, 0), (2020, 7, 4.8, 'VIETNAM: SON LA PROVINCE', 20.872, 104.541, 0, 0, 0, 0), (2020, 7, 7.8, 'USA: ALASKA', 55.03, -158.522, 0, 0, 0, 0), (2020, 8, 5.1, 'USA: NORTH CAROLINA:  SPARTA', 36.476, -81.094, 0, 0, 0, 0), (2020, 8, 6.6, 'PHILIPPINES:  MASBATE', 12.021, 124.123, 1, 0, 48, 0)]


line = (2020, 3, 5.4, 'BALKANS NW:  CROATIA:  ZAGREB', 45.897, 15.966, 1, 0, 27, 6000.0)
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
    file = [line for line in csv.reader(fp)]
    for i, line in enumerate(file):
        line = [x if x != '' else 0 for x in line]
        ints = [line[2], line[3], line[23], line[25], line[27]]
        floats = [line[9], line[20], line[21], line[29]]
        try:
            year = int(line[2])
            month = int(line[3])
            magnitude = float(line[9])
            location = line[19]
            latitude = float(line[20])
            longitude = float(line[21])
            deaths = int(line[23])
            missing = int(line[25])
            injuries = int(line[27])
            damages = float(line[29])
            tup = (year, month, magnitude, location, latitude,
                   longitude, deaths, missing, injuries, damages)
            file[i] = tup
        except ValueError:
            continue

    file = [x for x in file if isinstance(x, tuple)]

    return file

Student = read_file(open_file())

for i, val in enumerate(Student):
    if val != Instructor[i]:
        print(i)
        print('student', val)
        print('Instructor', Instructor[i])
        print()
        print('student prev', Student[i-1])
        print('instructor prev', Instructor[i - 1])
        print()