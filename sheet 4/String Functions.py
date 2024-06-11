a, b = [int(i) for i in input().split(" ")]
x = list(input())
lst =[]

for i in range(b):
    instruction = input()
    if "pop_back" in instruction:
        x.pop(-1)
    elif "front" in instruction:
        lst.append(x[0])
    elif "back" in instruction:
        lst.append(x[-1])
    elif :
