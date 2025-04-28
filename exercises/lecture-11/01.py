import time

# Декоратор, що затримує виконання функції на задану кількість секунд
def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)  # Затримка перед виконанням функції
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Функція, яка буде декорована
@delay(5)
def it_may_be(name=''):
    return f"{name} ask: It's nearly Luncheon Time? \n"

# Виклик функції через цикл
for t in range(12):
    print(it_may_be(name='Winnie-the-Pooh'))

