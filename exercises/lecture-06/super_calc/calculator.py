from helpers import extract, calc_help, result

def run_calculator():
    entry = input("Enter x operator y (e.g., 2 + 2): ")
    a, b, operator = extract(entry)

    if not operator:
        calc_help("Invalid format or unsupported operator.")
        return

    res, err = result(a, b, operator)
    if err:
        print(err)
    else:
        print(f"{a} {operator} {b} = {res}")
