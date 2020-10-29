def list_to_tuple(original):
    print(tuple(map(int, original)) if not any(not x.isdigit() for x in
                                               original) else 'Error. Please enter only integers.')


def main():
    a_list = input(
        "Enter elements of list separated by commas: ").strip().split(',')
    list_to_tuple(a_list)


main()