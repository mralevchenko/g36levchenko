# Константи для переведення
FEET_TO_INCHES = 12
FEET_TO_YARDS = 0.333333333
FEET_TO_MILES = 0.000189393939

# Введення відстані в футах
distance_in_feet = float(input("Input distance in feet: "))

# Обчислення
distance_in_inches = distance_in_feet * FEET_TO_INCHES
distance_in_yards = distance_in_feet * FEET_TO_YARDS
distance_in_miles = distance_in_feet * FEET_TO_MILES

# Виведення результатів
print(f"The distance in inches is {distance_in_inches} inches.")
print(f"The distance in yards is {distance_in_yards} yards.")
print(f"The distance in miles is {distance_in_miles} miles.")

