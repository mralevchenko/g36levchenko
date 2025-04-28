def average(*args):
    return sum(args) / len(args) if args else 0

# Основна частина з input
def get_numbers_input():
    input_str = input("Введіть числа через пробіл: ")
    return [float(x) for x in input_str.split()]

try:
    numbers = get_numbers_input()
    print("Середнє значення:", average(*numbers))
except ValueError:
    print("Будь ласка, введіть тільки числа.")
