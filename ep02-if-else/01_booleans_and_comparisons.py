# Episode 2 - Booleans and comparisons
# Code & Curious: Python, Visually

# True and False are BOOLEANS (type: bool). Note the capital T and F.
print(type(True))      # <class 'bool'>
print(int(True))       # 1
print(int(False))      # 0

# The 6 comparison operators. Each one gives back True or False.
print(7 > 2)     # True    greater than
print(7 < 2)     # False   less than
print(5 >= 5)    # True    greater than or equal to
print(4 <= 3)    # False   less than or equal to
print(5 == 5)    # True    equal to?
print(5 != 3)    # True    NOT equal to?

# A comparison result is a real value: you can store it in a variable
is_big = 5 > 3
print(is_big)    # True

# =  TELLS (assignment)    ==  ASKS (comparison)
age = 18             # put the name tag "age" on the value 18
print(age == 18)     # is age equal to 18?  -> True
