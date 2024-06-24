x = input()
lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]

if sum(lst1) == sum(lst2):
    print("Yes")
else:
    print("No")