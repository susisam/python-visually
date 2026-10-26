# Life in Numbers | Code & Curious: Python, Visually Ep 1
name = input("What is your name? ")
age = int(input("How old are you? "))

days = age * 365
hours = days * 24
heartbeats = hours * 60 * 70   # about 70 beats per minute

print(f"Hi {name}! Here is your life in numbers:")
print(f"Days lived:  about {days:,}")
print(f"Hours lived: about {hours:,}")
print(f"Heartbeats:  about {heartbeats:,}")

# Tip: {days:,} adds commas to big numbers, e.g. 9125 -> 9,125
