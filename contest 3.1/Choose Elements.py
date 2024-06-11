n, k = [int(i) for i in input().split(" ")]
lst = [int(i) for i in input().split(" ")]

summation = []
for i in range(k):
    k = max(lst)
    summation.append(k)
    lst.remove(k)

print(sum(summation))
