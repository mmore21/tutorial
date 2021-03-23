s = str(input('Enter any word or set of characters!'))
count = 0
iteration = 0
bob = 'bob'

while iteration <= len(s):
    if bob in s[iteration: iteration + 3]:
        count += 1
    iteration += 1

print('Number of times bob occurs is: ', str(count))
