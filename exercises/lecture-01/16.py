# Зчитуємо оригінальну ціну товару та знижку
price = float(input())  # Оригінальна ціна товару
discount = float(input())  # Відсоток знижки

# Обчислюємо нову ціну з урахуванням знижки
new_price = price * (1 - discount)

# Виводимо результат
print(new_price)

