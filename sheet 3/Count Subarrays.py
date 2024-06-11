testCases = int(input())
lst = []

while(testCases):
    lenght = int(input())
    nums = [int(i) for i in input().split(" ")]

    conc = []
    for i in range(1, lenght+1):
        for z in range(lenght):
            conc_ = nums[z: z+i]
            if len(conc_) >= i:
                conc.append(conc_)

    lst.append(conc)
    testCases -= 1

count_lst = []
for i in lst:
    count = 0
    for w in i:
        flag = False
        for z in range(len(w) -1):
            if not (w[z] < w[z +1]):
                flag = True
        if not flag:
            count += 1
    count_lst.append(count)

print(*count_lst, sep= "\n")
