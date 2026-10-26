# Episode 1: Your First Program, Under the Hood

**Python, Visually** by Code & Curious: a beginner Python series where you see what your code actually does inside the computer.

## Files

| File | What it shows |
|---|---|
| `01_hello.py` | Your first program: `print("Hello, World!")` |
| `02_bytecode_peek.py` | Under the hood: the bytecode the Python Virtual Machine runs |
| `03_errors.py` | `SyntaxError` and `NameError`, made on purpose |
| `04_variables_and_memory.py` | Variables as name tags, `id()`, garbage collection |
| `05_data_types_and_binary.py` | `int`, `float`, `str`, `bool`, binary, the `0.1 + 0.2` surprise |
| `06_strings.py` | Strings as sequences, indexing, `ord()`, immutability |
| `07_input_and_conversion.py` | `input()`, the string trap, `int()`, f-strings |
| `life_in_numbers.py` | Mini project: Life in Numbers |
| `challenge.py` | Your challenge: add breaths (about 16 per minute) |

## How to run

```bash
python life_in_numbers.py      # Windows
python3 life_in_numbers.py     # Mac / Linux
```

## Computer science concepts in this episode

- **Sequential execution:** a program runs its instructions one after another, top to bottom.
- **Binary and bits:** processors only understand 0s and 1s (transistors switching off and on).
- **Compiler vs interpreter:** translate the whole program first, or translate and run step by step.
- **Bytecode and the PVM:** Python compiles to bytecode, which the Python Virtual Machine executes. That's why the same code runs on Windows, macOS and Linux.
- **Standard output (stdout):** where `print()` sends text, which the operating system connects to your terminal.
- **References:** a variable is a name that points to an object in memory.
- **Garbage collection:** objects that nothing points to can be freed (CPython counts references).
- **Binary numbers and bytes:** 25 = 16 + 8 + 1 = `11001`, and 8 bits make 1 byte.
- **Floating-point precision:** `0.1` can't be stored exactly in binary, so compare floats with `math.isclose()`.
- **Sequences and O(1) access:** strings are indexed from 0, and indexing takes constant time (the same idea as arrays).
- **Immutability:** strings can't be changed in place, so you make a new one.

## Next episode

**Episode 2: If & Else.** How computers make decisions.
