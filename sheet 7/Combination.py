def factorial(x):
    if x == 1:
        return 1
    if x == 0:
        return 1
    else:
        return x * factorial(x -1)
    
def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


n, r = [int(i) for i in input().split(" ")]
print(combination(n, r))