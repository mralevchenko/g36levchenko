def sum_by(lst, fn):
    return sum(map(fn, lst))

# --- Основна частина з input ---

import ast  # Безпечніша альтернатива eval

try:
    input_str = input("Введіть список словників у форматі [{ 'n': 4 }, { 'n': 2 }, ...]: ")
    lst = ast.literal_eval(input_str)

    if not isinstance(lst, list) or not all(isinstance(item, dict) and 'n' in item for item in lst):
        raise ValueError("Список повинен містити лише словники з ключем 'n'.")

    result = sum_by(lst, lambda v: v['n'])
    print("Сума:", result)

except Exception as e:
    print("Помилка:", e)
