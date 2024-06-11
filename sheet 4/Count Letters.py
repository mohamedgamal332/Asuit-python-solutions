x = input()

dic = {chr(i + 97) : 0 for i in range(26)}
print(dic)
for i in x:
    dic[i] += 1
dic = {i: dic[i] for i in dic if (dic[i] != 0)}
sorted_dic = sorted(dic)

dic = {sorted_dic_item : dic[sorted_dic_item] for sorted_dic_item in sorted_dic}

for i, v in dic.items():
    print(f"{i} : {v}")