# Under the hood: Python compiles your code to BYTECODE,
# then the Python Virtual Machine (PVM) runs it one instruction at a time.
# The "dis" module (short for disassembler) lets you see that bytecode.

import dis

source = 'print("Hello, World!")'
code = compile(source, "hello.py", "exec")   # step 1: compile to bytecode
dis.dis(code)                                # look at the instructions
exec(code)                                   # step 2: the PVM runs them

# Note: the exact instruction names can differ slightly between Python versions.
