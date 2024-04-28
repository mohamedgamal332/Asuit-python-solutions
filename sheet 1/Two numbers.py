import math
y = input().split(" ")
div = int(y[0]) / int(y[1])

print(f"floor {y[0]} / {y[1]} = {math.floor(div)}")
print(f"ceil {y[0]} / {y[1]} = {math.ceil(div)}")
frac = math.ceil(div) - div
if frac == 0.5:
    print(f"round {y[0]} / {y[1]} = {math.ceil(div)+1}")
else:
    print(f"round {y[0]} / {y[1]} = {round(div)}")


"""
floor 10 / 4 = 2
ceil 10 / 4 = 3
round 10 / 4 = 3
"""