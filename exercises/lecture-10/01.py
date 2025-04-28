import math

class Circle:
    def __init__(self, x, y, r):
        """Ініціалізує коло з центром у точці (x, y) та радіусом r."""
        self.x = x
        self.y = y
        self.set_r(r)  # Використовуємо set_r для перевірки радіусу

    def length(self):
        """Повертає довжину кола."""
        return 2 * math.pi * self.r

    def square(self):
        """Повертає площу кола."""
        return math.pi * self.r ** 2

    def set_r(self, r):
        """Встановлює радіус кола. Перевіряє, що радіус є позитивним числом."""
        if r <= 0:
            raise AssertionError("Радіус має бути позитивним числом!")
        self.r = r


# --- Основна частина з input ---

def get_circle_input():
    try:
        x = float(input("Введіть координату x центру кола: "))
        y = float(input("Введіть координату y центру кола: "))
        r = float(input("Введіть радіус кола: "))
        return Circle(x, y, r)
    except ValueError:
        print("Будь ласка, введіть коректні числові значення!")
        return None
    except AssertionError as e:
        print(e)
        return None

# Створення кола через input
circle = get_circle_input()

if circle:
    print("Довжина кола:", circle.length())
    print("Площа кола:", circle.square())
