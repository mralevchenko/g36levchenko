import argparse

# Створення парсера
parser = argparse.ArgumentParser(
    description='Display a square of a given number',
    usage='square.py number [-h]'
)

# Додаємо позиційний аргумент
parser.add_argument('number', type=int, help='display a square of a given number')

# Парсимо аргументи
args = parser.parse_args()

# Обчислюємо квадрат
print(f"The square of {args.number} is {args.number ** 2}")
