# Зчитуємо введені значення
days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# Перетворюємо все в секунди
total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

# Виводимо результат
print(f"The amounts of seconds: {total_seconds}")

