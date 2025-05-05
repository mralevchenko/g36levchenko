# Зчитуємо платню і податок
salary = float(input())  # Платня (грн)
tax = float(input())  # Податок у відсотках

# Обчислюємо чисту зарплату
net_salary = salary * (1 - tax / 100)

# Виводимо результат
print(net_salary)

