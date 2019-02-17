import os
import game


def mainMenu():
    os.system("clear")
    print("\n" * 9)
    print("Welcome to the Tic Tackity Toe".center(80, " "))
    print("[1] Player vs AI    ".center(80, " "))
    print("[2] Player vs Player".center(80, " "))
    print("[3] Play test AI    ".center(80, " "))
    print("[4] Exit game       ".center(80, " "))
    print("\n" * 9)

    while True:
        player_input = input("> ")

        if player_input == "1":
            with_ai = True
            game.playGame(with_ai)

        if player_input == "2":
            with_ai = False
            game.playGame(with_ai)

        if player_input == "3":
            print(playTest())

        if player_input == "4":
            exit()


def playTest():
    # Player first
    player_win = 0
    player_lose = 0
    player_draw = 0
    for i in range(1, 10001):
        result = game.playTestAi("X")

        if result == "draw":
            player_draw += 1

        if result == "O":
            player_win += 1

        if result == "X":
            player_lose += 1

    # Ai first
    ai_win = 0
    ai_lose = 0
    ai_draw = 0
    for i in range(1, 10001):
        result = game.playTestAi("O")

        if result == "draw":
            ai_draw += 1

        if result == "O":
            ai_win += 1

        if result == "X":
            ai_lose += 1

    return f"Player first - Wins: {player_win}, Draw: {player_draw}, Loss {player_lose}\nAi first - Wins: {ai_win}, Draw: {ai_draw}, Loss {ai_lose}"
