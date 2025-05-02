import random
import time

def game():
    num_t_guess = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    print("Я хочу сыграть с тобой в игру 𓁹‿𓁹 ХЕХ. Я загадал число от 0 до 100, попробуй угадать.")

    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1

            if guess < num_t_guess:
                print("Моё число больше.")
            elif guess > num_t_guess:
                print("Моё число меньше.")
            else:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"Молодец ( ദ്ദി ˙ᗜ˙ ) Ты угадал за {attempts} попыток и за {duration} секунд.")
                save_stats(attempts, duration, True)
                break
        except ValueError:
            print("Nuh-uh. Введи целое число.")

def save_stats(attempts, duration, won):
    with open("GG_stats.txt", "a", encoding="utf-8") as f:
        result = "Победа" if won else "Проигрыш"
        f.write(f"Результат: {result}, Попыток: {attempts}, Время: {duration} сек. \n")

while True:
        game()
        again = input("Хочешь сыграть снова? (Да/Нет): ").capitalize()
        if again != "Да":
            print("Спасибо за игру! ( ´ཀ` )ᯓ★")
            break
