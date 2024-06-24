x = input()

org = int(x)
last = int("".join(list(x)[0:-1]))
blast = int("".join(list(x)[0:-2] + [x[-1]]))
print(max([org, last, blast]))