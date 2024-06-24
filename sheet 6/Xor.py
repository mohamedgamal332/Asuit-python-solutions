a, b, q = [int(i) for i in input().split(" ")]

def Qth(q):
    if q == 1:
        return a
    elif q == 2:
        return b

    return (Qth(q-1)) ^ Qth(q-2)


print(Qth(q))