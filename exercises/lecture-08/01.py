# Генераторна функція для нескінченної послідовності Фібоначчі
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

# Створення списку до значення 610
fib_list = []

for n in fib():
    if n > 610:
        break
    fib_list.append(n)

print(fib_list)
