input_coordinats = open('input.txt', 'r').readlines()
depth, horizontal = 0, 0
aim = 0

for i in input_coordinats:
    command, steps = i.split()
    if command == "up":
        depth -= int(steps)
    elif command == "down":
        depth += int(steps)
    else:
        horizontal += int(steps)
        aim += (int(steps) * depth)

#print(depth * horizontal)
print(aim * horizontal)
