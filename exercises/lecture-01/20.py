def convert_seconds(seconds):
    # Обчислюємо кількість днів, годин, хвилин і секунд
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    # Повертаємо результат у вигляді рядка
    return f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)."

# Вхідні дані
times = [6785, 456789, 86401]

# Обробка кожного значення і виведення результату
for time in times:
    print(convert_seconds(time))

