

VOWELS = 'aeiou'
s = input().lower()
while s != 'quit':
    new_s = ''
    for i, let in enumerate(s):
        if s[i] in VOWELS:
            if i == 0:
                new_s += s + 'way'
                break
            else:
                new_s += s[i:] + s[:i] + 'ay'
                break
        else:
            continue
    print(new_s)
    s = input().lower()
