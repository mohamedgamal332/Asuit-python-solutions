word = list(input())

for i in range(len(word)):
    if word[i] == "?":
        word[i] = word[-(i +1)]

print("".join(word))