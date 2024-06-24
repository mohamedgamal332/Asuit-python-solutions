x = input()

lst = [int(i) for i in input().split(" ")]

untreated = 0
cruits = 0


for i in lst:
    if i > 0:
        cruits += i
    if cruits > 0 and i == -1:
        cruits -= 1
        continue
        
    if i == -1 and cruits == 0:
        untreated += 1

print(untreated)