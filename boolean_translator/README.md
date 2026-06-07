# Boolean Logic to Three-Address Code (TAC) Translator

This project implements the "Front-End" and "Middle-End" of a compiler that translates Boolean expressions into Three-Address Code (TAC).
It features a Lexical Analyzer (Lexer) and a Recursive Descent Parser (Parser) that strictly enforce operator precedence (NOT > AND > OR, XOR).

## Prerequisites

- Python 3.x installed on your system.

## Setup and Execution

1. Open a terminal or command prompt in the directory containing `translator.py`.
2. Run the script by passing a Boolean expression as an argument.

### Single Expression Example:

```bash
python translator.py "NOT (a OR b) AND (c OR d)"
```

**Output:**
```
Input: NOT (a OR b) AND (c OR d)

Output:
t1 = a OR b
t2 = NOT t1
t3 = c OR d
t4 = t2 AND t3
RESULT = t4
```

### Running Given Tests
To run all the standard test cases defined in the assignment (which includes the custom operator `XOR`), use the `--test` flag:

```bash
python translator.py --test
```

## Features

- **Operators Supported**: `NOT`, `AND`, `OR`, and a custom `XOR` operator.
- **Precedence enforced**: 
  - `NOT` (Highest, right-associative)
  - `AND` (Medium, left-associative)
  - `OR` / `XOR` (Lowest, left-associative)
- **Parenthetical Grouping**: Overrides default precedence (e.g., `(a OR b)`).
- **Operands supported**: Identifiers (`x`, `y`, `var_1`) and Boolean literals (`TRUE`, `FALSE`).

- **Output format**: The translator emits Three-Address Code (TAC) lines using temporaries `t1, t2, ...` and a final `RESULT = <expr>` line. Boolean literals are emitted as lowercase `true`/`false` in TAC.
