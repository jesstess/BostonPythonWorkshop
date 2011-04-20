import re

VOWELS = ['a', 'e', 'i', 'o', 'u']

WORD_LIST = "words.txt"
words = file(WORD_LIST, 'r').readlines()
# Get rid of newlines
words = [word.strip() for word in words]

# Print all words that have a q that is not followed by a u.
for word in words:
    if 'q' in word.lower():
        if 'qu' not in word.lower():
            print word

# Print all words that have no vowels
for word in words:
    has_vowel = False
    for vowel in VOWELS:
        if vowel in word.lower():
            has_vowel = True
    if not has_vowel:
        print word

#######
# Suggested exercises
#######

# Find and print the words that start with "ee".

# Checking substrings by hand:
for word in words:
    if word.lower()[:2] == "ee":
        print word

# Using a regular expression:
pattern = re.compile("^ee")
for word in words:
    if pattern.search(word.lower()):
        print word

# Find and print the words that end in "mt". How about "gry"?

# Checking substrings by hand:
for word in words:
    if word.lower()[-2:] == "mt":
        print word

for word in words:
    if word.lower()[-3:] == "gry":
        print word

# Using a regular expression:
pattern = re.compile("mt$")
for word in words:
    if pattern.search(word.lower()):
        print word

pattern = re.compile("gry$")
for word in words:
    if pattern.search(word.lower()):
        print word

# Find an print the words that contain 4 or more 'l's.
pattern = re.compile("l(.*)l(.*)l(.*)l")
for word in words:
    if pattern.search(word.lower()):
        print word

# Find and print the words that have all 5 vowels in alphabetical
# order.
pattern = re.compile("a(.*)e(.*)i(.*)o(.*)u")
for word in words:
    if pattern.search(word.lower()):
        print word
