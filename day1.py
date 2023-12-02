def advent_of_code_loser(args: str) -> int:
    ans = 0
    result = []
    for i, c in enumerate(args):
        if c.isdigit():
            result.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if args[i:].startswith(val):
                result.append(str(d+1))
    ans = int(result[0] + result[-1])
    return ans


with open('input.txt', 'r') as Files:
    score = 0
    for lines in Files:
        lines = lines.strip()
        score += advent_of_code_loser(lines)
    print(score)
