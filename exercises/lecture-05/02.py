# Відкриваємо файл для читання
with open('file.txt', 'r') as file:
    # Зчитуємо всі рядки з файлу
    lines = file.splitlines()

# Вставляємо нове речення після другого рядка
lines.insert(2, "If Peter Piper picked a peck of pickled peppers.")

# Відкриваємо новий файл для запису зміненого вмісту
with open('new_file.txt', 'w') as new_file:
    # Записуємо змінені рядки в новий файл
    new_file.write("\n".join(lines))
