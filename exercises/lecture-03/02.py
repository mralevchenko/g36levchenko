def min_n(lst, n):
    sorted_lst = sorted(lst)
    return sorted_lst[:n]

# Ввід користувача
input_list = input("Введіть елементи списку через пробіл: ")
lst = list(map(int, input_list.split()))
n = int(input("Введіть кількість найменших елементів (n): "))

result = min_n(lst, n)
print(f"{n} найменших елемент(и):", result)
