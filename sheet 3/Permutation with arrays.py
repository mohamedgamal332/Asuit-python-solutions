x = int(input())
y1 = [int(i) for i in input().split(" ")]
y2 = [int(i) for i in input().split(" ")]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
    
y1 = quicksort(y1)
y2 = quicksort(y2)

if y1 == y2:
    print("yes")
else:
    print("no")        