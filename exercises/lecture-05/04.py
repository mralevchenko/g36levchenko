import argparse

# Створення парсера аргументів
parser = argparse.ArgumentParser(
    prog='square.py',
    usage='square.py number [-h]',
    description='',
    add_help=False  # Вимикаємо стандартну допомогу, щоб додати свою
)

# Додаємо позиційний аргумент — число
parser.add_argument(
    'number',
    type=int,
    help='display a square of a given number'
)

# Додаємо опцію -h / --help вручну
parser.add_argument(
    '-h', '--help',
    action='help',
    default=argparse.SUPPRESS,
    help='show this help message and exit'
)

# Розбір аргументів
args = parser.parse_args()

# Обчислення квадрата
print(args.number ** 2)
