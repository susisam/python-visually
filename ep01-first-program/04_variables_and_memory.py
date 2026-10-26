# Variables are NAME TAGS that point to objects in memory, not boxes.

name = "Asha"
age = 25
print(name, age)

# id() gives an object's identity. In standard Python (CPython)
# this is its memory address. Your numbers will be different.
print("id of age before:", id(age))

age = 26          # Python creates/finds the object 26 and MOVES the tag
print("id of age after: ", id(age))   # a different id!

# Two names can point to the SAME object:
other = age
print(other is age)   # True: both tags point to one object

# Objects with no names pointing to them can be freed automatically.
# This is garbage collection. CPython does it mainly by counting references.
