import random

user_input = input('Type "Roll" to roll the dice!')

while "Roll" in user_input:
        a = 2
        b = 12
        x = random.randint(a, b)
        print('You rolled', x, '!')
        user_input = input('Type "Roll" to roll again!')
        if user_input == "Roll":
            continue
        else:
            print('Thanks for playing!')

if user_input != "Roll":
    print('Sorry, you can not play!')
