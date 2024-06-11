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

for f in lst:
    print(*[max(i) for i in f], sep= " ")
