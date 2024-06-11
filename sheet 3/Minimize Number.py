x = int(input())

y = [int(i) for i in input().split(" ")]
count = 0

def check_all_even(x):
    for i in range(len(x)):
        if (x[i] % 2 != 0):
            return False
    return True

while(check_all_even(y)):    
    count += 1
    for i in range(len(y)):
        y[i] = y[i] / 2
    
print(count)