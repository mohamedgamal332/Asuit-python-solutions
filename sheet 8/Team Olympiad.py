x = input()

lst = [int(i) for i in input().split(" ")]

program = 0
math = 0
pe = 0

for i in lst:
    if i == 1:
        program += 1
    elif i == 2:
        math += 1
    else:
        pe += 1

num_teams = min([program, math, pe])
res = []


for i in range(num_teams):
    tmp_lst = []

    pr = lst.index(1)
    m = lst.index(2)
    pee = lst.index(3)

    tmp_lst.append(pr)
    tmp_lst.append(m)
    tmp_lst.append(pee)

    lst.remove(1)
    lst.remove(2)
    lst.remove(3)
    res.append(tmp_lst)

print(*res, sep="\n")