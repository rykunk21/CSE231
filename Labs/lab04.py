def leap_year(s):
    return (int(s) % 400 == 0) or (int(s) % 4 == 0 and int(s) % 100 != 0)


def rotate(s, n):
    new_s = s[-n:] + s[:-n]
    return new_s


def digit_count(s):
    import math
    evens, odds = '2468', '13579'
    s = math.floor(s); s = str(s)
    even_count, odd_count, zero_count = 0, 0, 0
    for i, ch in enumerate(s):
        if ch in evens:
            even_count += 1
        elif ch in odds:
            odd_count += 1
        elif ch == '0':
            zero_count += 1
    return even_count, odd_count, zero_count


def float_check(s):

    return s.isdigit() if '.' not in s else s.count('.') == 1 if not any(let.isalpha() for let in s) else False


if __name__ == '__main__':
    print(leap_year(input('Leap Year\n')))
    print(rotate(input('\nRotate\n').split()))
    print(digit_count(float(input('\nDigit Count\n'))))
    print(float_check(input('\nFloat Check\n')))
