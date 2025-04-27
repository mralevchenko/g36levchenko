def roll(lst, n):
    if not lst:
        return []
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

# Ввід користувача
input_list = input("Введіть елементи списку через пробіл: ")
lst = list(map(int, input_list.split()))

n = int(input("Введіть кількість елементів для переміщення (n): "))

# Результат
result = roll(lst, n)
print("Результат:", result)
