x = input().split(" ")
first = float(x[0])
second = float(x[1])

if first == 0 and second == 0:
    print("Origem")
elif first == 0:
    print("Eixo Y")
elif second ==0:
    print("Eixo X")
elif first > 0 and second > 0:
    print("Q1")
elif first < 0 and second > 0:
    print("Q2")
elif first < 0 and second < 0:
    print("Q3")
elif first > 0 and second < 0:
    print("Q4")

