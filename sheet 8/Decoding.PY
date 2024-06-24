x = input()
word = list(input())


def median_f(word):
    median = 0
    if len(word) % 2 == 0:
        median = len(word) // 2 - 1
    else:
        median = len(word) // 2
    return median

new_lst = []

for i in range(len(word)):
    median = median_f(word)
    new_lst.append(word.pop(median))

for i in range(len(new_lst)):
    median = median_f(new_lst)
    word.append(new_lst.pop(median))

print("".join(word))
