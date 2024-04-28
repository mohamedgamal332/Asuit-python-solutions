x = int(input())

days = (x % 365) % 30 
months = int(((x - days) % 365) / 30)
years = int(((x - days) - months * 30) / 365)

print(f"{years} years")
print(f"{months} months")
print(f"{days} days")