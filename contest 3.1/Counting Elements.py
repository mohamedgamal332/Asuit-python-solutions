x = int(input())
inputs_list = [int(i) for i in input().split(" ")]

dif_list = [0]
for i in range(1, x):
    dif_list.append(inputs_list[i] - inputs_list[i -1])

print(dif_list.count(1) + inputs_list.count())