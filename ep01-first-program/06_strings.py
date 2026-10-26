# Strings are SEQUENCES: characters stored in order, like seats in a row.
word = "Python"

# Indexing starts at 0
print(word[0])     # 'P'
print(word[5])     # 'n'
# Getting any index takes the same time: O(1), constant time (just like arrays)

# Negative indexes count from the end
print(word[-1])    # 'n'  (always the last character)
print(word[-6])    # 'P'

print(len(word))   # 6

# Each character is stored as a number (a Unicode code point)
print(ord("A"))    # 65
print(chr(65))     # 'A'

# Strings are IMMUTABLE: you cannot change a character in place.
# word[0] = "J"    # TypeError: 'str' object does not support item assignment
new_word = "J" + word[1:]   # make a NEW string instead
print(new_word)    # Jython
