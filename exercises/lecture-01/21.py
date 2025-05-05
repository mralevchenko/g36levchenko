def convert_to_time(n):
    hours = n // 60  # Кількість годин
    minutes = n % 60  # Кількість хвилин
    return hours, minutes

# Вхідні дані
times = [150, 25, 440]

# Обробка і виведення результатів
for time in times:
    hours, minutes = convert_to_time(time)
    print(hours, minutes)

