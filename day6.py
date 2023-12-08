for i in range(0, 31):
    print(i)
    print((30-i) * i)
    print("============")


with open('input6.txt', 'r') as Files:
    para = Files.readlines()
    text1 = para[0].split(':')[1].strip().split('    ')
    text2 = para[1].split(':')[1].strip().split('   ')
    dd = dict()
    for i in range(len(text1)):
        time = int(text1[i].strip())
        dis = int(text2[i].strip())
        dd[dis] = time
    aa = dict()
    str1 = ""
    str2 = ""
    for distance, timer in dd.items():
        counter = 0
        str1 += str(distance)
        str2 += str(timer)
        for i in range(timer+1):
            if (timer-i) * i >= distance:
                counter += 1
        aa[distance] = counter
    ans = 1
    for _mx, x in aa.items():
        ans *= x
    print(ans)
    num1 = int(str1)
    num2 = int(str2)
    counter1 = 0
    for i in range(num2+1):
        if (num2-i) * i >= num1:
            counter1 += 1
    print(counter1)
