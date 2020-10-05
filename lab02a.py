#######################################
#   Lab 02
#   Algorithm
#       Prompt the user for a integer
#       check that integer for multiple conditions
#       check n amount of integers until the user stops
#       calculate and display data related to all the input
#       terminate the program
#######################################

n_str = int(input("Input an integer (0 terminates): "))
odds = []                                  # store all odd numbers in a list
evens = []                                  # store all even numbers in a list
odd_cnt = 0
even_cnt = 0
positive_int_count = 0

while n_str != 0:                              # loops until the user inputs 0
    if n_str < 0:
       print('Try a positive number')
    elif n_str % 2 == 0:                         # checks for even value
        even_cnt += 1
        evens.append(n_str)
    elif n_str % 2 != 0:                       # checks for odd value
        odd_cnt += 1
        odds.append(n_str)
    if n_str > 0:                              # checks for positive
        positive_int_count += 1
    n_str = int(input("Input an integer (0 terminates): "))

odd_sum = sum(odds)
even_sum = sum(evens)
odd_count = len(odds)
even_count = len(evens)

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
