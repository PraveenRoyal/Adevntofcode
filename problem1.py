def first_two_digits(calibration: str) -> int:
    """
    Parse a string to give first and last digits in the string
    """
    num = []
    for c, l in enumerate(calibration):
        if l.isalpha():
            continue
        num.append((c, int(l)))
    return num


# a = 0
# a = first_two_digits('1abc2')
# print(a)
# a = first_two_digits('pqr3stu8vwx')
# print(a)
# a = first_two_digits('a1b2c3d4e5f')
# print(a)
# a = first_two_digits('treb7uchet')
# print(a)


def string_number_finder(args: str) -> list:
    """it takes a string and checks for the
    index of all the numbers that are written
    in strings"""
    numbers_in_words = ['one', 'two', 'three', 'four',
                        'five', 'six', 'seven', 'eight'
                        'nine']
    finder = []
    for lof, a in enumerate(numbers_in_words):
        m = args.find(a)
        if m == -1:
            continue
        finder.append((m, lof+1))

    return finder


# alist = string_number_finder('eighttwothree')
# print(alist)


def order_list_parser(a: list, b: list):
    """here the function merges two lists
    and returns the values from the lists"""
    a.extend(b)
    sorted_list = sorted(a, key=lambda x: x[0])
    _, ans = sorted_list[0]
    _, bns = sorted_list[-1]
    return int(str(ans) + str(bns))


first = first_two_digits('7eight8twothree')
second = string_number_finder('7eight8twothree')


lm = order_list_parser(first, second)
print(lm)


# with open('input.txt', 'r') as File:
#     sum_of_numbers = 0
#     for files in File:
#         a = files.strip()
#         first_of = first_two_digits(a)
#         second_of = string_number_finder(a)
#         b = order_list_parser(first_of, second_of)
#         sum_of_numbers = sum_of_numbers + b
#     print(sum_of_numbers)

t_list = ['two1nine',
         'eighttwothree',
         "abcone2threexyz",
         'xtwone3four',
         '4nineeightseven2',
         'zoneight234',
         '7pqrstsixteen'
          ]

sum_of = 0
for mx in t_list:
    first_of = first_two_digits(mx)
    second_of = string_number_finder(mx)
    b = order_list_parser(first_of, second_of)
    sum_of += b
print(sum_of)
for c, l in enumerate('abcdefg'):
    print(c, l)
