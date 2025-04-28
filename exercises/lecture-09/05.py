def average_by(lst, fn=lambda x: x):
    return sum(map(fn, lst)) / len(lst) if lst else 0

# --- Основна частина з input ---
def get_dict_input():
    input_str = input("Введіть список словників (наприклад, [{'n': 4}, {'n': 2}]): ")
    import ast
    return ast.literal_eval(input_str)

try:
    lst = get_dict_input()
    print("Середнє значення:", average_by(lst, lambda x: x['n']))
except Exception as e:
    print("Помилка:", e)

