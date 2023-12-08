example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
s = example.splitlines()
a = s[0].split(':')
b = a[1].strip().split('|')
print(b)
num = b[0].strip().split(' ')
set1 = set()
for each in num:
    set1.add(int(each))
print(set1)
num1 = b[1].strip().split(' ')
set2 = set()
print(num1)
for e in num1:
    if not e.isdigit():
        continue
    set2.add(int(e))
print(set2)
inter = set1.intersection(set2)
print(inter)


def extract_numbers(string: str) -> int:
    """take a string and gives lenght of the
    intersection of numbers between two sides"""
    string_num = string.split(':')
    only_num = string_num[1].split('|')
    first = only_num[0].split(' ')
    set1 = set()
    for each in first:
        if not each.isdigit():
            continue
        set1.add(int(each))
    second = only_num[1].split(' ')
    set2 = set()
    for each in second:
        if not each.isdigit():
            continue
        set2.add(int(each))
    inter = set1.intersection(set2)
    return len(inter)


def summer(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return summer(num-1)+summer(num-1)


total = 0
for sx in s:
    num = extract_numbers(sx)
    total += summer(num)
    print(num)
print(total)

total_sum = 0
with open('input4.txt', 'r') as Files:
    for line in Files:
        line = line.strip()
        num = extract_numbers(line)
        total_sum += summer(num)
print(total_sum)


with open('input4.txt', 'r') as Files:
    card_to_track = {}
    for num, line in enumerate(Files):
        if num not in card_to_track:
            card_to_track[num] = 1
        line = line.strip()
        extrac_num = extract_numbers(line)
        for m in range(num + 1, num + extrac_num+1):
            card_to_track[m] = card_to_track.get(m, 1) + card_to_track[num]
    total = sum(card_to_track.values())
    print(total)
