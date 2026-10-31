# Episode 1: Your First Program, Under the Hood

Code for Episode 1 of **Python, Visually** on the Code & Curious channel. In this series we don't just write Python, we look at what actually happens inside the computer when it runs.

## What's in this folder

| File | What it's about |
|---|---|
| `01_hello.py` | The classic first program, `print("Hello, World!")` |
| `02_bytecode_peek.py` | A peek at the bytecode the Python Virtual Machine runs |
| `03_errors.py` | A `SyntaxError` and a `NameError`, made on purpose |
| `04_variables_and_memory.py` | Variables as name tags, `id()` and garbage collection |
| `05_data_types_and_binary.py` | `int`, `float`, `str`, `bool`, binary, and the `0.1 + 0.2` surprise |
| `06_strings.py` | Strings as sequences, indexing, `ord()` and immutability |
| `07_input_and_conversion.py` | `input()`, the string trap, `int()` and f-strings |
| `life_in_numbers.py` | The mini project from the video |
| `challenge.py` | Your challenge: add breaths (roughly 16 a minute) |

## Running the code

Open a terminal in this folder and type:

```bash
python life_in_numbers.py      # Windows
python3 life_in_numbers.py     # Mac / Linux
```

Swap in any other file name to run that one.

## The ideas behind this episode

A program runs one instruction after another, top to bottom. Underneath, the processor only understands 0s and 1s, which is why your code has to be translated. Some languages translate the whole program first (a compiler), others translate and run as they go (an interpreter).

Python does a bit of both. It first turns your code into bytecode, and the Python Virtual Machine runs that bytecode. That's the reason the same script works on Windows, macOS and Linux.

When you call `print()`, the text goes to standard output, and the operating system shows it in your terminal.

A variable isn't a box. It's a name pointing at an object in memory. When nothing points at an object any more, Python frees it (CPython does this mostly by counting references).

Numbers are stored in binary. 25 is 16 + 8 + 1, or `11001`, and 8 bits make a byte. Some decimals can't be stored exactly, which is why `0.1 + 0.2` isn't quite `0.3`. Use `math.isclose()` when you compare floats.

Strings are sequences, counted from 0. Jumping to any position takes the same time no matter how long the string is (O(1), just like arrays). You also can't change a string in place, you build a new one.

## Up next

Episode 2: If and Else, or how a computer makes decisions.
