# input() pauses the program and returns what the user typed, ALWAYS as a string.
name = input("What is your name? ")
print(f"Hello, {name}!")

# The trap: adding strings JOINS them (concatenation)
a = input("First number: ")
b = input("Second number: ")
print("Without int():", a + b)    # 5 and 5 -> 55

# The fix: TYPE CONVERSION with int()
a = int(a)
b = int(b)
print("With int():   ", a + b)    # 5 and 5 -> 10

# f-strings: put f before the quotes and variables inside { }
age = 25
print(f"In 10 years you will be {age + 10}.")
