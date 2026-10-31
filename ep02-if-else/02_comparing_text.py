# Comparing text is CASE-SENSITIVE
print("apple" == "apple")   # True
print("Apple" == "apple")   # False

# Why? Each character is stored as a number:
print(ord("A"))   # 65
print(ord("a"))   # 97
