from ops.arithmetic import ops

def extract(entry):
    for o in ops:
        if o in entry:
            parts = entry.split(o)
            if len(parts) == 2:
                return parts[0].strip(), parts[1].strip(), o
    return None, None, None

def calc_help(e=''):
    if e:
        print(f"\n{e}")
    print("""
    Usage operation:
        h                        Display this usage message
        2 + 2                    Add
        3 - 1                    Subtract
        2 * 2                    Multiply
        4 / 2                    Divide
        5 // 2                   Int Divide
        7 % 3                    Modulo Divide
        2 ** 3                   Exponentiation
        q                        Quit
    """)

def result(a, b, operator):
    try:
        a, b = float(a), float(b)
        if operator == '/' and b == 0:
            return None, "Oops, division by zero"
        elif operator in ('//', '%') and b == 0:
            return None, "Oops, division or modulo by zero"
        return ops[operator](a, b), ''
    except ValueError:
        return None, "Invalid input. Please enter numeric values."
