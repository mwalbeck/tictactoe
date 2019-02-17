import os
import menu
import ai
import random


def hasWon(board, player):
    win_cons = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for win_con in win_cons:
        if (
            board[win_con[0]] == player
            and board[win_con[1]] == player
            and board[win_con[2]] == player
        ):
            return True


def isDraw(board):
    for space in board:
        if space != "X" and space != "O":
            return False
    return True


def printBoard(board):
    os.system("clear")
    print("\n" * 9)
    print(f"{board[0]}|{board[1]}|{board[2]}".center(80, " "))
    print("-+-+-".center(80, " "))
    print(f"{board[3]}|{board[4]}|{board[5]}".center(80, " "))
    print("-+-+-".center(80, " "))
    print(f"{board[6]}|{board[7]}|{board[8]}\n".center(80, " "))
    print("\n" * 8)


def validInput(player_input):
    if not player_input.isnumeric():
        return False

    if not int(player_input) > 0 or not int(player_input) < 10:
        return False

    return True


def validMove(board, player_input):
    if board[player_input - 1] != "X" and board[player_input - 1] != "O":
        return True

    return False


def makeMove(board, player, player_input):
    board[player_input - 1] = player


def playAgain():
    print("Do you want to play again? (Y/N)")
    user_input = input("> ")

    if user_input == "y" or user_input == "Y":
        return True

    menu.mainMenu()


def getPlayerMove(player, board):
    while True:
        print(f"Player {player}'s turn:")
        player_input = input("> ")

        if not validInput(player_input):
            print("Please type in a number between 1 and 9.")
            continue

        clean_input = int(player_input)

        if validMove(board, clean_input):
            return clean_input

        print("This spot is already taken, please pick another.")


def playGame(with_ai):
    player = random.choice(["X", "O"])
    board = list(range(1, 10))

    while True:
        printBoard(board)

        if player == "X":
            makeMove(board, player, getPlayerMove(player, board))

        if player == "O" and with_ai:
            makeMove(board, player, ai.getComputerMove(board, player))
        elif player == "O":
            makeMove(board, player, getPlayerMove(player, board))

        if hasWon(board, player):
            printBoard(board)
            print(f"Player {player} has won!!!!!!!!!!!!!!!!!!!!!")
            if playAgain():
                playGame(with_ai)
            break

        if isDraw(board):
            printBoard(board)
            print("It's a draw!")
            if playAgain():
                playGame(with_ai)
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


def playTestAi(start_player):
    player = start_player
    board = list(range(1, 10))

    while True:
        if player == "X":
            makeMove(board, player, ai.getComputerMove(board, player))

        if player == "O":
            makeMove(board, player, ai.getComputerMove(board, player))

        if hasWon(board, player):
            return player

        if isDraw(board):
            return "draw"

        if player == "X":
            player = "O"
        else:
            player = "X"
