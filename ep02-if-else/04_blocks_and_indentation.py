# Indentation groups lines into a BLOCK
temperature = 35

if temperature > 30:
    print("It's a hot day!")   # part of the block
    print("Drink water.")      # part of the block
print("Done!")                 # NOT indented: always runs

# Forget the indentation and Python stops with:
# IndentationError: expected an indented block after 'if' statement
