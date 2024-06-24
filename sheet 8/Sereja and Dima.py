x = int(input())
lst = [int(i) for i in input().split(" ")]

l = 0
r = len(lst) -1

sereji = 0
dima = 0

player1 = "sereji"
player2 = "dima"
current_player = ""

for i in range(x):
    current_player = player2 if current_player == player1 else player1
    if lst[r] <= lst[l]:
        
        if current_player == "sereji":
            sereji += lst[l]
        else:
            dima += lst[l]
        
        l += 1
    elif lst[r] > lst[l]:

        if current_player == "sereji":
            sereji += lst[r]
        else:
            dima += lst[r]
        
        r -= 1

print(sereji, dima)