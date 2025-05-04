from pathlib import Path

# Вкажіть назву файлу
file_path = Path("yourfile.txt")  # Замініть на свою назву файла

# Перевірка, чи існує файл
if file_path.exists():
    text = file_path.read_text(encoding='utf-8')  # Читання вмісту

    num_lines = text.count('\n') + 1 if text else 0
    num_words = len(text.split())
    num_chars = len(text)

    print(f"Файл: {file_path.name}")
    print(f"Рядків: {num_lines}")
    print(f"Слів: {num_words}")
    print(f"Символів: {num_chars}")
else:
    print(f"Файл '{file_path}' не знайдено.")
