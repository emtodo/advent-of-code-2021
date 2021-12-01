increased = 0
increased_by_three = 0
input_depths = open('measurments.txt', 'r').readlines()
depths = [int(x) for x in input_depths]

# Part 1
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        increased += 1

# And a one-liner for part 1
print(sum([1 for i in range(1, len(input_depths)) if int(input_depths[i]) > int(input_depths[i - 1])]))

# Part 2
for i in range(3, len(depths)):
    if depths[i] > depths[i - 3]:
        increased_by_three += 1

# One-liner for part 2
print(sum([1 for i in range(3, len(input_depths)) if int(input_depths[i]) > int(input_depths[i - 3])]))

print(increased)
print(increased_by_three)

