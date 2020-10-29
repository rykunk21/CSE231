#####################################
# Computer Project #3
#
# Take user input to get information about their student life
# Use this information to compute the students tuition
#
# Algorithm
#   Define 4 different functions:
#       upperclassman / underclassman
#       resident / non-resident
#           this will prevent an error from trying to pass an argument into a
#           function if that argument wasn't prompted, breaking your code
#   Massive boolean loop to check if the user wants to continue
#   using a series of if else statements, prompt the user for input and call
#   the corresponding function based off which input is provided
#   check if the user wants to continue. if no, terminate the code
#####################################


def resident_under_classman_tuition_cost( year, credits):
    """ if the user is a resident, and an underclassman, use this function
    to compute their tuition cost"""
    total_cost = 0

    RESIDENT_FRESHMAN_PER_CREDIT = 482
    RESIDENT_FRESHMAN_FLAT_RATE = 7230

    RESIDENT_SOPHOMORE_PER_CREDIT = 494
    RESIDENT_SOPHOMORE_FLAT_RATE = 7410

    if year == 'freshman':
        if credits < 12:
            total_cost += credits * RESIDENT_FRESHMAN_PER_CREDIT
        elif 12 <= credits <= 18:
            total_cost += RESIDENT_FRESHMAN_FLAT_RATE
        elif credits > 18:
            total_cost += RESIDENT_FRESHMAN_FLAT_RATE
            total_cost += (credits - 18) * RESIDENT_FRESHMAN_PER_CREDIT
    elif year == 'sophomore':
        if credits < 12:
            total_cost += credits * RESIDENT_SOPHOMORE_PER_CREDIT
        elif 12 <= credits <= 18:
            total_cost += RESIDENT_SOPHOMORE_FLAT_RATE
        elif credits > 18:
            total_cost += RESIDENT_SOPHOMORE_FLAT_RATE
            total_cost += (credits - 18) * RESIDENT_SOPHOMORE_PER_CREDIT

    return total_cost


def resident_upper_classman_tuition_cost(college, credits):
    """ if the user is a resident, and an upperclassman, use this function
    to compute their tuition cost"""
    total_cost = 0

    RESIDENT_CORE_UPPERCLASSMAN_PER_CREDIT = 555
    RESIDENT_CORE_UPPERCLASSMAN_FLAT_RATE = 8325
    RESIDENT_BROAD_UPPERCLASSMAN_PER_CREDIT = 573
    RESIDENT_BROAD_UPPERCLASSMAN_FLAT_RATE = 8595

    if college == 'business' or college == 'engineering':
        if credits < 12:
            total_cost += credits * RESIDENT_BROAD_UPPERCLASSMAN_PER_CREDIT
        elif 12 <= credits <= 18:
            total_cost += RESIDENT_BROAD_UPPERCLASSMAN_FLAT_RATE
        elif credits > 18:
            total_cost += RESIDENT_BROAD_UPPERCLASSMAN_FLAT_RATE
            total_cost += (credits - 18) * \
                          RESIDENT_BROAD_UPPERCLASSMAN_PER_CREDIT
    else:
        if credits < 12:
            total_cost += credits * RESIDENT_CORE_UPPERCLASSMAN_PER_CREDIT
        elif 12 <= credits <= 18:
            total_cost += RESIDENT_CORE_UPPERCLASSMAN_FLAT_RATE
        elif credits > 18:
            total_cost += RESIDENT_CORE_UPPERCLASSMAN_FLAT_RATE
            total_cost += (credits - 18) * \
                          RESIDENT_CORE_UPPERCLASSMAN_PER_CREDIT


    return total_cost


def non_resident_underclassman_tuition_cost(credits, international):
    """ if the user is not a resident, and an underclassman, use this function
    to compute their tuition cost"""
    total_cost = 0

    INTERNATIONAL_SPECIAL_FEE_PART_TIME = 375
    INTERNATIONAL_SPECIAL_FEE_FULL_TIME = 750

    INTERNATIONAL_UNDERCLASSMAN_PER_CREDIT = 1325.5
    INTERNATIONAL_UNDERCLASSMAN_FLAT_RATE = 19883

    if credits < 12:
        total_cost += credits * INTERNATIONAL_UNDERCLASSMAN_PER_CREDIT
    elif 12 <= credits <= 18:
        total_cost += INTERNATIONAL_UNDERCLASSMAN_FLAT_RATE
    elif credits > 18:
        total_cost += INTERNATIONAL_UNDERCLASSMAN_FLAT_RATE
        total_cost += (credits - 18) * INTERNATIONAL_UNDERCLASSMAN_PER_CREDIT

    if international:
        if credits <= 4:
            total_cost += INTERNATIONAL_SPECIAL_FEE_PART_TIME
        else:
            total_cost += INTERNATIONAL_SPECIAL_FEE_FULL_TIME


    return total_cost


def non_resident_upperclassman_tuition_cost(credits, international):
    """ if the user is not a resident, and an upperclassman, use this function
    to compute their tuition cost"""
    total_cost = 0

    INTERNATIONAL_SPECIAL_FEE_PART_TIME = 375
    INTERNATIONAL_SPECIAL_FEE_FULL_TIME = 750


    INTERNATIONAL_UPPERCLASSMAN_PER_CREDIT = 1366.75
    INTERNATIONAL_UPPERCLASSMAN_FLAT_RATE = 20501

    if credits < 12:
        total_cost += credits * INTERNATIONAL_UPPERCLASSMAN_PER_CREDIT
    elif 12 <= credits <= 18:
        total_cost += INTERNATIONAL_UPPERCLASSMAN_FLAT_RATE
    elif credits > 18:
        total_cost += INTERNATIONAL_UPPERCLASSMAN_FLAT_RATE
        total_cost += (credits - 18) * INTERNATIONAL_UPPERCLASSMAN_PER_CREDIT

    if international:
        if credits <= 4:
            total_cost += INTERNATIONAL_SPECIAL_FEE_PART_TIME
        else:
            total_cost += INTERNATIONAL_SPECIAL_FEE_FULL_TIME

    return total_cost


def speicalfees(college, cmse, credits):
    """ This function should be called at the end to add on all the special
    fees to the tuition cost"""

    total_cost = 0

    HEALTH_OR_SCIENCE_SPECIAL_FEE_PART_TIME = 50
    HEALTH_OR_SCIENCE_SPECIAL_FEE_FULL_TIME = 100
    CMSE_SPECIAL_FEE_PART_TIME = 402
    CMSE_SPECIAL_FEE_FULL_TIME = 670
    BUSINESS_SPECIAL_FEE_PART_TIME = 113
    BUSINESS_SPECIAL_FEE_FULL_TIME = 226
    ENGINEERING_SPECIAL_FEE_PART_TIME = 402
    ENGINEERING_SPECIAL_FEE_FULL_TIME = 670

    if college == 'business':
        if credits <= 4:
            total_cost += BUSINESS_SPECIAL_FEE_PART_TIME
        else:
            total_cost += BUSINESS_SPECIAL_FEE_FULL_TIME
    elif college == 'engineering':
        if credits <= 4:
            total_cost += ENGINEERING_SPECIAL_FEE_PART_TIME
        else:
            total_cost += ENGINEERING_SPECIAL_FEE_FULL_TIME
    elif college == 'health' or college == 'sciences':
        if credits <= 4:
            total_cost += HEALTH_OR_SCIENCE_SPECIAL_FEE_PART_TIME
        else:
            total_cost += HEALTH_OR_SCIENCE_SPECIAL_FEE_FULL_TIME
    elif cmse:
        if credits <= 4:
            total_cost += CMSE_SPECIAL_FEE_PART_TIME
        else:
            total_cost += CMSE_SPECIAL_FEE_FULL_TIME

    return total_cost


def tax(total, credits, james_madison):
    """ This function should be called at the end to add on all the taxes
    to the tuition cost"""
    if james_madison:
        total += 7.5
    if credits >= 6:
        total += 5
    total += 21
    total += 3

    return total


def assign_bool(s):
    """ this function is used to assign True or False when a user puts inputs
    yes or no. This function will also return None if the user inputs
    anything besides yes or no, and we can use this return value to check
    the user input infinitely until we get yes or no, saving a ton of
    redundant coding"""
    s = s.lower()
    if s == 'yes':
        s = True
    elif s == 'no':
        s = False
    else:
        print("Invalid input. Try again.")
        return None
    return s


# given that a lot of the lines are super long, assigning the prompt text to a
# variable, allowing the code to be more concise
print("2019 MSU Undergraduate Tuition Calculator.\n")

residency_prompt = "Resident (yes/no): "

intern_prompt = "International (yes/no): "

grade_prompt = "Enter Level as freshman, sophomore, junior, senior: "

college_prompt = "Enter college as business, engineering, health, sciences, " \
                 "or none: "

cmse_prompt = 'Is your major CMSE ("Computational Mathematics and ' \
              'Engineering") (yes/no): '

engineering_prompt = "Are you admitted to the College of Engineering (" \
                     "yes/no): "

james_madison_prompt = "Are you in the James Madison College (yes/no): "

cont_prompt = "Do you want to do another calculation (yes/no): "

cont = True  # assign the continue variable to be initially true, to start
# the loop

james_madison = False  # assign all the boolean values to expected default
# output, just in case we don't prompt for these variables, and then we can
# pass through default values into our function
engineering = False
college = ''
international = False
cmse = False

while cont:  # start the loop and prompt the user for the required input
    residency = assign_bool(input(residency_prompt))
    while residency is None:
        residency = assign_bool(input(residency_prompt))

    if not residency:  # now that all our yes / no input can be assigned to
        # boolean values, we can do really quick efficient checks with if else
        international = assign_bool(input(intern_prompt))
        while international is None:
            international = assign_bool(input(intern_prompt))

    while True:  # loop ensures the grade input is valid
        grade = input(grade_prompt).lower()
        if (grade == 'freshman') or (grade == 'sophomore') or \
                (grade == 'junior') or (grade == 'senior'):
            break
        else:
            print("Invalid input. Try again.")
            continue

    if grade == 'junior' or grade == 'senior':
        while True:  # checks the upperclassman college
            college = input(college_prompt).lower()
            if (college == 'business') or college == 'engineering' or \
                    (college == 'health') or (college == 'sciences'):
                break
            else:
                college = None
                break
        cmse = assign_bool(input(cmse_prompt))
        while cmse is None:
            cmse = assign_bool(input(cmse_prompt))

    elif grade == 'freshman' or grade == 'sophomore':  # checks if freshman /
        # sophomores are admitted to the engineering college
        engineering = assign_bool(input(engineering_prompt))
        while engineering is None:
            engineering = assign_bool(input(engineering_prompt))

    if (college == 'business') or (college == 'engineering') or \
            (college == 'health') or (college == 'sciences'):
        pass
    else:
        james_madison = assign_bool(input(james_madison_prompt))
        while james_madison is None:
            james_madison = assign_bool(
                input(james_madison_prompt))

    college_credits = input("Credits: ")  # checks how many credits the user
    # has and will keep prompting until you reach successful output,
    # and then set that value to an integer
    while college_credits == '0' or not college_credits.isdigit():
        print("Invalid input. Try again.")
        college_credits = input("Credits: ")
    college_credits = int(college_credits)

    if residency:  # run a series of checks to determine which function to
        # call, then call that function and print the function output plus
        # special fees plus tax
        if grade == 'freshman' or grade == 'sophomore':
            tuition = (resident_under_classman_tuition_cost(grade,
                                                            college_credits))
            tuition += speicalfees(college, cmse, college_credits, )

            print('Tuition is ${:,.2f}.'.format(
                tax(tuition, college_credits, james_madison)))
        else:
            tuition = (resident_upper_classman_tuition_cost(college,
                                                            college_credits))
            tuition += speicalfees(college, cmse, college_credits, )
            print(
                'Tuition is ${:,.2f}.'.format(
                    tax(tuition, college_credits, james_madison)))
    else:
        if grade == 'freshman' or grade == 'sophomore':
            tuition = (non_resident_underclassman_tuition_cost(college_credits,
                                                               international))
            tuition += speicalfees(college, cmse, college_credits, )
            print(
                'Tuition is ${:,.2f}.'.format(
                    tax(tuition, college_credits, james_madison)))
        else:
            tuition = (non_resident_upperclassman_tuition_cost(college_credits,
                                                               international))
            tuition += speicalfees(college, cmse, college_credits,)
            print(
                'Tuition is ${:,.2f}.'.format(
                    tax(tuition, college_credits, james_madison)))

    cont = assign_bool(input(cont_prompt))   # check if the user wants to
    # continue
    while cont is None:
        cont = assign_bool(input(cont_prompt))
