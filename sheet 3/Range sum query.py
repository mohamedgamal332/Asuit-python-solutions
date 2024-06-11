a, b = [int(i) for i in input().split(" ")]
inputs = [int(i) for i in input().split(" ")]
outputs = []
prop_sum = [0] * a


for i in range(a):
    if i == 0:
        prop_sum[i] = inputs[i]
    else:
        prop_sum[i] = inputs[i] + prop_sum[i -1]
        

for i in range(b):
    lower, upper = [int(i) for i in input().split(" ")]
    outputs.append(prop_sum[upper -1] - prop_sum[lower -1] + inputs[lower -1])

print(*outputs, sep= "\n")  