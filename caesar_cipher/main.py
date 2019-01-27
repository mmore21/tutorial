'''
---------------------------------------------
|   Author  :   Maz                         |
|   Created :   September 11, 2018          |
|   Program :   Caesar Cipher               |
---------------------------------------------
'''

# alphabets used for computing cipher
alphaLower = 'abcdefghijklmnopqrstuvwxyz'
alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create empty cipher string to be filled later
cipher = ''

# get phrase string from user
phrase = input('Enter a phrase to encrypt: ')

# initialize key to false value
key = 0
while (key < 0 or key > 25):
    key = int(input('Enter a key (1-25) to encode phrase: '))

# create list of characters from input
chars = list(phrase)

# iterate over every character in list
for char in chars:
    # character is a lower alpha
    if (char in alphaLower):
        pos = alphaLower.index(char) + key
        # retain position within alphabet boundaries
        if (pos > 25):
            pos -= 26
        cipher += alphaLower[pos]
    # character is an upper alpha
    elif (char in alphaUpper):
        pos = alphaUpper.index(char) + key
        # retain position within alphabet boundaries
        if (pos > 25):
            pos -= 26
        cipher += alphaUpper[pos]
    # character is non-alpha
    else:
        cipher += char

print("Cipher:", cipher)