n, m = [int(i) for i in input().split(" ")]
lst = [int(i) for i in input().split(" ")]



def suffix_sum(arr, m):
    if m <= 0:
        return 0
    else:
        return arr[len(arr) - m] + suffix_sum(arr, m - 1)



print(suffix_sum(lst, m))