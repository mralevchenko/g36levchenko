def every_nth(lst, n):
    return lst[n-1::n]

# Отримуємо список від користувача у вигляді рядка і перетворюємо на список чисел
input_list = input("Введіть елементи списку через пробіл: ")
lst = list(map(int, input_list.split()))

# Отримуємо n
n = int(input("Введіть число n: "))

# Викликаємо функцію та друкуємо результат
result = every_nth(lst, n)
print(f"Кожен {n}-й елемент списку:", result)
