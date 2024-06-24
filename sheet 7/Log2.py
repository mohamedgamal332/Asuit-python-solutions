def log2(x):
    if x > 1:
        return 1 + log2(x // 2)
    else:
        return 0
    
print(log2(int(input())))
