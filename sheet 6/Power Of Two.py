def power_of_two(x):
    if x == 1.0:
        return True
    elif x < 1:
        return False
    return power_of_two(x/2)

x = float(input())
print("YES" if power_of_two(x) else "NO")
