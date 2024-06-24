# Pyramid  

def pyramid(x, n =1):
    if x > 0:
        print(" " * (x -1), end= "")
        print("*" * n, end= "")
        print("")
        return pyramid(x -1, n +2)
    

pyramid(int(input()))
