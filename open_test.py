

with open('test.txt', 'r') as test:
    for line in test.readlines():
        print(line.replace('\n', '').replace(' ', ''),end='')
