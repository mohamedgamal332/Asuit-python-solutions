import math
a, b = [int(x) for x in input().split(" ")]
div = (a / b)

print(f"floor {a} / {b} = {math.floor(div)}")
print(f"ceil {a} / {b} = {math.ceil(div)}")
frac = math.ceil(div) - div
if frac > 0.5:
    print(f"round {a} / {b} = {math.floor(div)}")
else:
    print(f"round {a} / {b} = {math.ceil(div)}")
