limak, bob = [int(i) for i in input().split(" ")]


def rec(limak, bob, n):
    if limak <= bob:
        return rec(limak * 3, bob * 2, n +1)
    else:
        return n


print(rec(limak, bob, 0)) 
