string = input()
ref = ['h','e','l','l','o']
index = 0
for i in range(len(string)):
    if string[i] == ref[index]:
        index += 1
        if index == len(ref) -1:
            print("YES")
            break

if index != len(ref) -1:
    print("NO")