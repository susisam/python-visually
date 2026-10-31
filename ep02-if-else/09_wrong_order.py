# A bug caused by the ORDER of conditions
marks = 95

if marks >= 50:        # True for 95, so this wins...
    grade = "C"
elif marks >= 75:      # ...and these are never even checked
    grade = "B"
elif marks >= 90:
    grade = "A"

print("Grade:", grade)   # Grade: C  (wrong!)
