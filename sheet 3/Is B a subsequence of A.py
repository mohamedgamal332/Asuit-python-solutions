n, m = [int(i) for i in input().split(" ")]
seq1 = input().split(" ")
seq2 = input().split(" ")


count2 = 0
for i in seq1:
    if i == seq2[count2]:
        count2 += 1


if count2 == m:
    print("YES")
else:
    print("NO")
