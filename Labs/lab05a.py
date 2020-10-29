#################################
## CSE 231
## Debug exercise for Lab 5
## print() not allowed
## @amirootyet
#################################


count = 0
max_height = 0
max_weight = 0
max_bmi = 0
min_height = None
min_weight = None
min_bmi = None

print('{:<12s}{:<12s}{:<12s}{:<12s}'.format('Name', 'Height(m)',
                                                  'Weight(kg)', 'BMI'))

with open('../data.txt') as fp1:  # open the file; set breakpoint
    total_height = 0  # keep track of total height
    total_weight = 0
    total_bmi = 0
    fp1.readline()
    for line in fp1:
        count += 1
        name, height, weight = line.split()

        height = float(height)
        weight = float(weight)
        bmi = weight / height ** 2
        total_bmi += bmi

        print(
            '{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}'.format(name, height,
                                                          weight, bmi))

        total_height += height
        total_weight += weight

        if min_height is None or height < min_height:
            min_height = height
        elif height > max_height:
            max_height = height
        if min_weight is None or weight < min_weight:
            min_weight = weight
        elif weight > max_weight:
            max_weight = weight
        if min_bmi is None or bmi < min_bmi:
            min_bmi = bmi
        elif bmi > max_bmi:
            max_bmi = bmi

average_height = total_height / count
average_weight = total_weight / count
average_bmi = total_bmi / count
print()

print('{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}'.format('Average',
                                                        average_height,
                                                        average_weight,
                                                        average_bmi))
print('{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}'.format('Max',
                                                        max_height,
                                                        max_weight,
                                                        max_bmi))
print('{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}'.format('Min',
                                                        min_height,
                                                        min_weight,
                                                        min_bmi))
