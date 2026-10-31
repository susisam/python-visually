# Mini project v2: handle the EDGE CASE (zero) first
number = int(input("Enter a number: "))
if number == 0:
    print("Zero is even, and neither positive nor negative.")
elif number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
