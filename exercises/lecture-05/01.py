# Відкриваємо файл sales.txt у режимі читання
with open('sales.txt', 'r') as file:
    # Зчитуємо всі рядки з файлу
    lines = file.readlines()

    # Перебираємо кожен рядок з файла
    for i, line in enumerate(lines, start=1):  # i - номер рядка, start=1 щоб рахувати з 1
        if 'laptop' in line:  # Перевіряємо, чи є 'laptop' у поточному рядку
            print(f"Номер рядка: {i}, Рядок: {line.strip()}")  # Виводимо номер та сам рядок

