from pathlib import Path

# Вказуємо шлях до файлу
path = Path('your_file.txt')  # замініть на реальну назву файла

# Читаємо вміст
text = path.read_text()

# Підрахунок
lines = text.count('\n') + 1 if text else 0  # кількість рядків
words = len(text.split())                   # кількість слів
characters = len(text)                      # кількість символів

# Вивід результату
print(f"Lines: {lines}")
print(f"Words: {words}")
print(f"Characters: {characters}")
