import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    print("Вгадай число від 1 до 100!")

    while True:
        try:
            guess = int(input("Введи свою спробу: "))

            if guess < 1 or guess > 100:
                print("Будь ласка, введи число в межах від 1 до 100.")
            elif guess < secret_number:
                print("Занадто маленьке. Спробуй більше.")
            elif guess > secret_number:
                print("Занадто велике. Спробуй менше.")
            else:
                print("Вітаю! Ти вгадав число! 🎉")
                break
        except ValueError:
            print("Будь ласка, введи ціле число.")

# Запуск гри
guess_the_number()
