import random

gameInput = input('Type "Roll" to roll the dice!')
testNum = gameInput

while "Roll" in testNum:
        a = 2
        b = 12
        x = random.randint(a, b)
        print('You rolled', x, '!')
        testNum = input('Type "Roll" to roll again!')
        if testNum == "Roll":
            continue
        else:
            print('Thanks for playing!')

if testNum != "Roll":
    print('Sorry, you can not play!')
