x = int(input())


def is_palindrome(s):
    return s == s[::-1]

def is_odd(n):
    return n % 2 != 0

if is_odd(x) and is_palindrome(bin(x)[2:]):
    print("YES")
else:
    print("NO")