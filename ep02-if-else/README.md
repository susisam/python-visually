# Episode 2: If & Else, How Computers Make Decisions

**Python, Visually** by Code & Curious: a beginner Python series where you see what your code actually does inside the computer.

## Files

| File | What it shows |
|---|---|
| `01_booleans_and_comparisons.py` | `True`/`False`, the 6 comparison operators, `=` vs `==` |
| `02_comparing_text.py` | Why text comparison is case-sensitive |
| `03_if_hot_day.py` | Your first `if` statement |
| `04_blocks_and_indentation.py` | Indentation and blocks |
| `05_if_else.py` | `else`: the other path |
| `06_can_i_vote.py` | Example: can I vote? |
| `07_under_the_hood.py` | The compare and jump instructions behind an `if` |
| `08_grades_elif.py` | `elif`: a grade calculator |
| `09_wrong_order.py` | Why the order of conditions matters |
| `10_modulo.py` | `%` (modulo): the remainder |
| `even_or_odd.py` | Mini project: Even or Odd? |
| `even_or_odd_v2.py` | Mini project v2: handling the edge case (zero) |
| `challenge.py` | Your challenge: a weather helper |

## How to run

```bash
python even_or_odd.py      # Windows
python3 even_or_odd.py     # Mac / Linux
```

## Computer science concepts in this episode

- **Booleans:** `True` and `False`, the `bool` type, named after George Boole. They match a single bit (1 or 0).
- **Comparison operators:** `>`, `<`, `>=`, `<=`, `==`, `!=`, each of which returns a boolean.
- **Assignment vs comparison:** `=` tells (puts a name tag on a value), `==` asks (are they equal?).
- **Case-sensitivity:** characters are stored as numbers (`ord("A")` is 65, `ord("a")` is 97).
- **Blocks:** Python groups lines with indentation (4 spaces) instead of `{ }`.
- **Flowcharts:** a diamond is a decision with True and False arrows.
- **Conditional jump (branching):** an `if` becomes a compare instruction plus a jump instruction, in bytecode and in machine code.
- **First True wins:** `if`/`elif` conditions are checked top to bottom, and the rest are skipped.
- **Modulo:** `%` gives the remainder, so `n % 2 == 0` means `n` is even.
- **Edge cases:** unusual inputs, like zero, that you handle first.

## Next episode

**Episode 3: and, or, not.** Combining conditions.
