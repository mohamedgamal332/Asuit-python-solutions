x = input().split(" ")

if (int(x[0]) > int(x[2])) and x[1] == ">":
    print("Right")
elif (int(x[0]) < int(x[2])) and x[1] == "<":
    print("Right")
elif int(x[0]) == int(x[2]) and x[1] == "=":
    print("Right")
else:
    print("Wrong")
