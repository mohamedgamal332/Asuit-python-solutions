x = int(input())

def sequence(x, n):
    if x == 1:
        return n
    elif x % 2 == 0:
        # even 
        return sequence(x // 2, n +1)
    else:
        # odd
        return sequence(3 * x + 1, n +1)

    

print(sequence(x, 1))