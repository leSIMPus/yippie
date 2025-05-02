import random

def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i])
        print(" " + row)
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def full(board):
    return all(cell != " " for row in board for cell in row)

def slayer(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    first = random.choice(["Игрок", "Компьютер"])

    if first == "Игрок":
        player_sym = "X"
        slayer_sym = "O"
        print("Ты играешь за крестики.")
        current_turn = "player"
    else:
        player_sym = "O"
        slayer_sym = "X"
        print("Ты играешь за нолики.")
        current_turn = "computer"

    while True:
        print_board(board)

        if current_turn == "player":
            try:
                row = int(input("Выбери строку (1-3): ")) - 1
                col = int(input("Выбери столбец (1-3): ")) - 1
                if board[row][col] != " ":
                    print("Эта клетка уже занята. Выбери другую.")
                    continue
            except (ValueError, IndexError):
                print("Некорретный ввод. Пожалуйста, введите число от 1 до 3.")
                continue

            board[row][col] = player_sym

            if check_winner(board, player_sym):
                print_board(board)
                print("Ты выиграл. Поздравляю!")
                break

            current_turn = "computer"

        else:
            print("Ход компьютера...")
            row, col = slayer(board)
            board[row][col] = slayer_sym

            if check_winner(board, slayer_sym):
                print_board(board)
                print("Компьютер оказался умнее. Ты проиграл.")
                break

            current_turn = "player"

        if full(board):
            print_board(board)
            print("Ничья.")
            break

while True:
    game()
    again = input("Желаешь сыграть снова? (Да/Нет): ").capitalize()
    if again != "Да":
        print("До встречи, спасибо за игру!")
        break