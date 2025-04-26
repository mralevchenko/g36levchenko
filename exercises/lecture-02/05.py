from decimal import Decimal, getcontext

# Встановимо точність обчислень (наприклад, 10 знаків після коми)
getcontext().prec = 10

def complex_interest(P, r, n, t):
    # Перетворюємо значення у Decimal
    P = Decimal(P)
    r = Decimal(r)
    n = Decimal(n)
    t = Decimal(t)
    

    amount = P * (1 + (r / n)) ** (n * t)
    return amount


P = input("Enter principal amount (P): ")
r = input("Enter annual interest rate (as decimal, e.g. 0.05 for 5%): ")
n = input("Enter number of times interest applied per year (n): ")
t = input("Enter number of years (t): ")

result = complex_interest(P, r, n, t)
print("Compound interest amount:", result)
