def sort_by_indexes(a, b, reverse=False):
    paired = zip(a, b)
    sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=reverse)
    return [item[0] for item in sorted_pairs]

# --- Основна частина з input ---
import ast

try:
    a_input = input("Введіть список значень (наприклад, ['eggs', 'bread', 'oranges']): ")
    b_input = input("Введіть список індексів (наприклад, [3, 2, 6]): ")

    a = ast.literal_eval(a_input)
    b = ast.literal_eval(b_input)

    if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b):
        raise ValueError("Обидва списки мають бути однакової довжини.")

    rev = input("Сортувати у зворотному порядку? (так/ні): ").strip().lower() == 'так'

    result = sort_by_indexes(a, b, reverse=rev)
    print("Відсортований список:")
    print(result)

except Exception as e:
    print("Помилка:", e)
