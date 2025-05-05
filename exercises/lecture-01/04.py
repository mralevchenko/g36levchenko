# Константи для переведення
FOOT_TO_CM = 30.48
INCH_TO_CM = 2.54

# Введення користувача
feet = int(input("Feet: "))
inches = int(input("Inches: "))

# Обчислення
height_cm = feet * FOOT_TO_CM + inches * INCH_TO_CM

# Виведення результату
print(f"Your height is: {height_cm:.1f} cm.")
