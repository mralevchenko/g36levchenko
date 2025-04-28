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


# --- Приклад використання ---

# Створення кола
c = Circle(3, 4, 1)

# Виведення довжини та площі кола
print(c.length(), c.square())  # 6.283185307179586 3.141592653589793

# Спроба встановлення від'ємного радіусу
try:
    c.set_r(-1)  # Очікується виключення
except AssertionError as e:
    print(e)  # Радіус має бути позитивним числом!

