def  PalArr(lst, r, l):
    if r != l:
        if lst[r] != lst[l]:   
            return "NO"
        return PalArr(lst, r +1, l-1)
    else:
        return "YES"
    
triv = int(input())
lst = [int(i) for i in input().split(" ")]
print(PalArr(lst, 0, triv -1))