def binary_search(arr, start, end, x):
    pivot = arr[(len(arr) -1) //2]

    if x > pivot and len(arr) > 2:
        return binary_search(arr[arr.index(pivot): ], x)
    elif x < pivot and len(arr) > 2:
        return binary_search(arr[: arr.index(pivot) +1], x)
    elif x == pivot or x == arr[arr.index(pivot) +1]:
        return True
    else: 
        return False
    
a, b = [int(i) for i in input().split(" ")]
y = [int(i) for i in input().split(" ")]
y.sort()

lst = []
for i in range(b):
    if binary_search(y, 0, len(y), int(input())):
        lst.append("found")
    else:
        lst.append("not found")

print(*lst, sep="\n")
