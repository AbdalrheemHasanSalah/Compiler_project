import sys
import re

tokens = []
pos = 0
t_counter = 1
lines = []


def tokenize(text: str):
    pattern = r'\bTRUE\b|\bFALSE\b|\bNOT\b|\bAND\b|\bOR\b|\bXOR\b|[a-zA-Z_]\w*|\(|\)'
    raw = re.findall(pattern, text, re.IGNORECASE)
    return [t.upper() for t in raw]


def next_tmp():
    global t_counter
    tmp = f"t{t_counter}"
    t_counter += 1
    return tmp


def is_valid(pos):
    return pos < len(tokens)


def peek():
    return tokens[pos] if is_valid(pos) else None


def eat(expected):
    global pos

    if is_valid(pos) and tokens[pos] == expected:
        pos += 1
    else:
        found = tokens[pos] if is_valid(pos) else "EOF"
        print(f"Error: expected {expected}, got {found}")
        sys.exit(1)



def parse_expression():
    lhs = parse_term()

    while peek() in ("OR", "XOR"):
        op = peek()
        eat(op)

        rhs = parse_term()
        tmp = next_tmp()
        lines.append(f"{tmp} = {lhs} {op} {rhs}")
        lhs = tmp

    return lhs



def parse_term():
    lhs = parse_factor()

    while peek() == "AND":
        eat("AND")

        rhs = parse_factor()
        tmp = next_tmp()
        lines.append(f"{tmp} = {lhs} AND {rhs}")
        lhs = tmp

    return lhs



def parse_factor():
    if peek() == "NOT":
        eat("NOT")

        val = parse_factor()
        tmp = next_tmp()
        lines.append(f"{tmp} = NOT {val}")
        return tmp

    return parse_primary()



def parse_primary():
    cur = peek()

    if cur in ("TRUE", "FALSE"):
        eat(cur)
        return cur.lower()

    if cur == "(":
        eat("(")
        val = parse_expression()
        eat(")")
        return val

    
    val = cur
    eat(cur)
    return val


def generate(expr: str):
    global tokens, pos, t_counter, lines

    tokens = tokenize(expr)
    pos = 0
    t_counter = 1
    lines = []

    result = parse_expression()
    return lines + [f"RESULT = {result}"]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ("--test", "--t"):
            tests = [
                "a AND b OR NOT c",
                "NOT (a OR b) AND (c OR d)",
                "x XOR y AND z"
            ]

            for t in tests:
                print(f"\nInput: {t}\nOutput:")
                for line in generate(t):
                    print(line)
                print("-" * 30)

        else:
            expr = " ".join(sys.argv[1:])
            print(f"Input: {expr}\nOutput:")
            for line in generate(expr):
                print(line)

    else:
        print("Please provide a logical expression.")
        print('Example: python translator.py "a AND b OR NOT c"')