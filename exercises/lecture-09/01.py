def sort_dict_by_key(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))

# --- Основна частина з input ---

# Ввід словника у вигляді рядка
input_str = input("Введіть словник у форматі {'ключ': значення, ...}: ")

try:
    d = eval(input_str)  

    if not isinstance(d, dict):
        raise ValueError("Це не словник!")

    # Вибір напрямку сортування
    direction = input("Сортувати за спаданням? (так/ні): ").strip().lower()
    reverse = direction == 'так'

    result = sort_dict_by_key(d, reverse=reverse)
    print("Відсортований словник:")
    print(result)

except Exception as e:
    print("Помилка:", e)
