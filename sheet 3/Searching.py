x = input()
lst = [int(x) for x in input().split(" ")]
target = int(input())

if target in lst:
    print(lst.index(target))
else:
    print(-1)