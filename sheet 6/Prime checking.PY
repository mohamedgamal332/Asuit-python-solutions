def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) +1):
            if x % i == 0:
                return False
        return True
    
x = int(input())
print("YES" if is_prime(x) else "NO")
    