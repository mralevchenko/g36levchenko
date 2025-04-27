def includes_any(lst, values):
    return any(val in lst for val in values)

# Ввід списків
lst_input = input("Введіть основний список (через пробіл): ")
values_input = input("Введіть значення для перевірки (через пробіл): ")

# Перетворення рядків на списки чисел
lst = list(map(int, lst_input.split()))
values = list(map(int, values_input.split()))

# Результат
result = includes_any(lst, values)
print("Результат перевірки:", result)
