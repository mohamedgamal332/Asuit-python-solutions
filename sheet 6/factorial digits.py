x = int(input())

lst = [int(i) for i in input().split(" ")]


def summ(lst):
    if not lst:
        return 0
    else:
        return lst[0] + summ(lst[1:])

print(summ(lst))