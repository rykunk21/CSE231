##############################################################################
# CSE 231
# Debug exercise for Lab 2
# print() not allowed
# @amirootyet
##############################################################################


# last, first = [x.strip() for x in input("Input a name: ").title().split(',')]; print(first[0]+'.', last)

while True:
    x = input("enter a word: ")
    y = x.lower()
    if y == 'quit':
        break
    else:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if x[0] in vowels:
            print(x + 'way')
        else:
            for i, j in enumerate(x):
                if j not in vowels:
                    pass
                else:
                    # using slice operation
                    print(x[i:] + x[0:i] + 'ay')
                    break
