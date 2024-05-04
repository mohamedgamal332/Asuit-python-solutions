x = int(input())
y = [int(i) for i in input().split(" ")]

count = 0

for i in y:
    if i == min(y):
        count +=1 

if count % 2 == 0:
    print("Unlucky")
else:
    print("Lucky")