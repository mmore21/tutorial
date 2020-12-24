import random
# for loop
end = random.randint(0, 10)
finalSum = end
for num in range(end):
    finalSum += num

print(finalSum)


# while loop
initial = 1
endSum = 0
end = random.randint(0, 10)

while initial <= end:
    endSum += initial
    initial += 1

print(endSum)
