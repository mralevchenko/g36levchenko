# Вводимо значення
f = float(input("Enter the desired future value: "))  # майбутня сума
r = float(input("Enter the annual interest rate: "))  # річна відсоткова ставка
n = int(input("Enter the number of years the money will grow: "))  # кількість років

# Обчислюємо поточну суму, яку потрібно внести
p = f / ((1 + r) ** n)

# Виводимо результат
print(f"You will need to deposit this amount: {p:.2f}.")

