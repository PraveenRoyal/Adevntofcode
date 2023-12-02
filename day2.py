text = "Game 15: 7 green, 4 blue, 3 red; 4 blue, 10 red, 1 green; 15 blue, 9 red"

# num = text[0].split(' ')[-1]
# print(num)
# rest = text[1].split(';')
# result = []
# for a in rest:
#     m = a.split(',')
#     for x in m:
#         x = x.strip()
#         y = x.split(' ')
#         result.append((y[1], int(y[0])))
# print(result)


def check_the_bag(args: str) -> int:
    """parse a string and check the numbers
    associated with colours

    :param args: str
    :returns: bool
    """
    dictionary = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    text = args.split(':')
   #  num = text[0].split(' ')[-1]
    rest = text[1].split(';')
    for color_sent in rest:
        colors = color_sent.split(',')
        for color in colors:
            color = color.strip()
            checker = color.split(' ')
            if int(checker[0]) > dictionary.get(checker[1]):
                dictionary.update({checker[1]: int(checker[0])})
    return dictionary.get('red') * dictionary.get('green') * dictionary.get('blue')


with open('input2.txt', 'r') as Files:
    ans = 0
    for text in Files:
        text = text.strip()
        checker = check_the_bag(text)
        ans += checker
    print(ans)

print(check_the_bag('Game 1: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'))
