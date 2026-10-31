# elif = "else if": more than two paths
marks = 80   # try 95, 75, 50, 30

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

# The FIRST True condition wins: Python runs that block and skips the rest.
# That's why the strictest check (>= 90) must come first.
