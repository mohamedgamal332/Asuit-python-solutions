testcases = int(input())
final = []
while(testcases):

    lst =[]
    x = int(input())
    y = [int(i) for i in input().split(" ")]
    for i in range(x):
        for z in range(i +1, x):
            lst.append(y[i] + y[z] + (z - i))

    final.append(lst)
    testcases -= 1

print(*[min(x) for x in final], sep ="\n")