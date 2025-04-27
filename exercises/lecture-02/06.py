from decimal import Decimal, getcontext

# Встановлюємо точність обчислень
getcontext().prec = 15

def EMI(P, annual_rate_percent, months):
    P = Decimal(P)
    r = Decimal(annual_rate_percent) / (12 * 100)  # місячна ставка
    n = Decimal(months)

    emi = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return emi

# Отримання вхідних даних від користувача
P = Decimal(input("Введіть суму позики (P): "))
rate = Decimal(input("Введіть річну відсоткову ставку (у %): "))
months = int(input("Введіть кількість місяців погашення (n): "))

# Розрахунок EMI
emi_value = EMI(P, rate, months)

# Вивід результату
print(f"EMI на {months} місяців: {emi_value}")
