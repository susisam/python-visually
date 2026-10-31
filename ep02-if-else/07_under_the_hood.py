# Under the hood: an if statement becomes COMPARE + JUMP instructions.
# Look for COMPARE_OP and POP_JUMP_IF_FALSE in the output.
import dis

source = '''
age = 20
if age >= 18:
    print("You can vote!")
else:
    print("Not yet!")
'''
dis.dis(compile(source, "vote_simple.py", "exec"))

# Note: instruction names can differ slightly between Python versions.
