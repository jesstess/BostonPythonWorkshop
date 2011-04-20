from string import ascii_lowercase
import re

VOWELS = ['a', 'e', 'i', 'o', 'u']

WORD_LIST = "words.txt"
words = file(WORD_LIST, 'r').readlines()
# Get rid of newlines
words = [word.strip() for word in words]

# Print all words containing 'uu'.
for word in words:
    if 'uu' in word.lower():
        print word

#######
# TODO: print all words that have a q that is not followed by a u.
#######

# Print all letters that never appear doubled in an English word.
for letter in ascii_lowercase:
    exists = False
    for word in words:
        if letter * 2 in word.lower():
            exists = True
            break
    if not exists:
        print "There are no English words with a double " + letter

# Print all words that have all 5 vowels.
for word in words:
    has_all_vowels = True
    for vowel in VOWELS:
        if vowel not in word.lower():
            has_all_vowels = False
            break
    if has_all_vowels:
        print word

#######
# TODO: print all words that have no vowels.
#######
        
# Print all words that are palindromes.
for word in words:
    if len(word) < 3:
        continue

    left_side = word[0:len(word) / 2]
    if len(word) % 2:
        # If it's an odd-length word, you don't care about the middle letter.
        right_side = word[len(word) / 2 + 1:]
    else:
        right_side = word[len(word) / 2:]
    right_side = right_side[::-1]
    if left_side == right_side:
        print word

# Use a regular expression to find and print all words containing 'uu'.
pattern = re.compile("uu")
for word in words:
    if pattern.search(word.lower()):
        print word

# Use a regular expression to find an print all words matching certain character
# constraints.
pattern = re.compile("^e.g....r$")
for word in words:
    if pattern.search(word.lower()):
        print word
