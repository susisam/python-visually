# Every value has a TYPE.
print(type(25))        # <class 'int'>   whole numbers
print(type(9.8))       # <class 'float'> decimals
print(type("Asha"))    # <class 'str'>   text
print(type(True))      # <class 'bool'>  True / False

# How 25 is stored in binary: 16 + 8 + 1 = 25  ->  11001
print(bin(25))         # '0b11001'
print(int("11001", 2)) # 25 (convert back from binary)
print(f"{25:08b}")     # 00011001  (8 bits = 1 byte)

# Python integers grow as big as your memory allows:
print(2 ** 100)        # 1267650600228229401496703205376

# The 0.1 + 0.2 surprise: 0.1 cannot be stored exactly in binary
print(0.1 + 0.2)               # 0.30000000000000004
print(0.1 + 0.2 == 0.3)        # False

import math
print(math.isclose(0.1 + 0.2, 0.3))   # True  -> compare floats like this
