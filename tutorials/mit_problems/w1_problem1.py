s = str(input("Enter a word to see how many vowels are in it."))
known_vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for vowel in s:
    if vowel in known_vowels:
        count += 1
        continue


print('Number of vowels: ', count)
