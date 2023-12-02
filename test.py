# Advent of code solutions day1
# problem 1 part 1
def parse_numbers(args: str) -> int:
    """this function parses the string and
    gives a number in return that correspond to
    first and last digit of the number
    :param args: str
    :returns: int

    """
    result = ""
    for alpha_num in args:
        if alpha_num.isalpha():
            continue
        result += alpha_num
    result = result[0] + result[-1]
    return int(result)


part1_answer = 0
with open('input.txt', 'r') as Files:
    for text in Files:
        text = text.strip()
        num = parse_numbers(text)
        part1_answer += num
print(part1_answer)


def string_to_number(args: str) -> list:
    """Returns a list of tuple
    with index and number as two tuple

    :param args: str
    :returns: list

    """
    result = []
    for index, num in enumerate(args):
        if num.isalpha():
            continue
        result.append((index, int(num)))
    return result


print(string_to_number('two1nine'))


def parse_str_number(args: str) -> list:
    """returns a two tuple of a number and
    index of a number
    :param args: str
    :returns: list
    """
    number_list = [
        'one',
        'two',
        'three',
        'four',
        'five'
        'six',
        'seven',
        'eight',
        'nine',
    ]
    result = []
    for number, num_str in enumerate(number_list):
        index = args.rfind(num_str)
        index2 = args.find(num_str)
        if index == -1 and index2 == -1:
            continue
        if index == index2:
            result.append((index, number+1))
        else:
            result.append((index, number+1))
            result.append((index2, number+1))
    return result


def parse_final(args: str) -> list:
    """returns a two tuple of a number and index
    of a number but using only find
    :param args: str
    :returns: list
    """
    result = []
    num_str = string_to_number(args)
    result.extend(num_str)
    str_num = parse_str_number(args)
    result.extend(str_num)
    result = sorted(result, key=lambda x: x[0])
    _, ans = result[0]
    _, bns = result[-1]
    final_str = str(ans) + str(bns)
    return int(final_str)


with open('input.txt', 'r') as Files:
    sum_of_all = 0
    for ans in Files:
        ans = ans.strip()
        sum_of_all += parse_final(ans)
    print(sum_of_all)
