def max_n(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[:n]

# Ввід користувача
input_list = input("Введіть елементи списку через пробіл: ")
lst = list(map(int, input_list.split()))
n = int(input("Введіть кількість найбільших елементів (n): "))

result = max_n(lst, n)
print(f"{n} найбільших елемент(и):", result)
