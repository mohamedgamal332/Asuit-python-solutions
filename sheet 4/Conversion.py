x = input()

for i in range(len(x)):
    x = x.replace(",", " ")
    x = x.swapcase()
print(x)