positions = input()
instructions = input()

count = 1

pos = 0
ins = 0

for i in range(len(instructions)):
    if instructions[ins] == positions[pos]:
        ins += 1
        pos += 1
        count += 1
    else:
        ins += 1

print(count)