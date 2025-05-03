import subprocess
import sys
def Choose():
    print("В какую игру вы хотите поиграть? 1 - Угадай число, 2 - Блэкджек, 3 - Крестики-нолик, 4 - На сегодня игр хватит...")


def run_game(game_file):
    subprocess.run([sys.executable, game_file])

def choose():
    while True:
        Choose()
        t = input("Введите номер:")
        if t == '1':
            run_game("Guess the Number.py")
        elif t == '2':
            run_game("Blackjack.py")
        elif t == '3':
            run_game("Tic Tac Toe.py")
        elif t == "4":
            print("До новых встреч!")
            break
        else:
            print("Такой игры у нас нет, попробуйте еще раз")

choose()