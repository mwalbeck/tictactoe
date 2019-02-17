import random
import game


def chooseRandomMove(board, moves):
    possible_move = []
    for move in moves:
        if game.validMove(board, move):
            possible_move.append(move)

    if possible_move:
        return random.choice(possible_move)

    return False


def cornerMove(board):
    return chooseRandomMove(board, [1, 3, 7, 9])


def edgeMove(board):
    return chooseRandomMove(board, [2, 4, 6, 8])


def randomFirstMove(board):
    move = random.randint(1, 3)

    if move == 1:
        return edgeMove(board)

    if move == 2:
        return cornerMove(board)

    if move == 3:
        return 5


def getBoardCopy(board):
    return board[:]


def whichTurn(board):
    turn_count = 0
    for space in board:
        if space == "X" or space == "O":
            turn_count += 1

    return turn_count + 1


def wentFirst(board):
    x_count = 0
    o_count = 0

    for space in board:
        if space == "X":
            x_count += 1
        if space == "O":
            o_count += 1

    if x_count == o_count:
        return True

    return False


def testCanWin(board, player, move):
    board_copy = getBoardCopy(board)
    game.makeMove(board_copy, player, move)
    if game.hasWon(board_copy, player):
        return True

    return False


def testCanFork(board, player, move):
    board_copy = getBoardCopy(board)
    board_copy[move - 1] = player
    winning_moves = 0
    for i in range(1, 10):
        if game.validMove(board_copy, i) and testCanWin(board_copy, player, i):
            winning_moves += 1

    return winning_moves >= 2


def getComputerMove(board, player):
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    # If Ai goes first, play certain moves
    if whichTurn(board) == 1:
        return randomFirstMove(board)

    # Check if AI can win with the next move
    for i in range(1, 10):
        if game.validMove(board, i) and testCanWin(board, player, i):
            return i

    # Check if Player can win with next move, so we can block them
    for i in range(1, 10):
        if game.validMove(board, i) and testCanWin(board, opponent, i):
            return i

    # Check AI fork moves
    for i in range(1, 10):
        if game.validMove(board, i) and testCanFork(board, player, i):
            return i

    # Check Player fork moves
    opponent_forks = 0
    for i in range(1, 10):
        if game.validMove(board, i) and testCanFork(board, opponent, i):
            opponent_forks += 1
            temp_move = i

    if opponent_forks == 1:
        return temp_move

    if opponent_forks == 2 and wentFirst(board):

        if board[2 - 1] == player or board[8 - 1] == player:
            return chooseRandomMove(board, [4, 6])

        if board[4 - 1] == player or board[6 - 1] == player:
            return chooseRandomMove(board, [2, 8])

    if opponent_forks == 2:
        return edgeMove(board)

    # Take the center if free
    if game.validMove(board, 5):
        return 5

    # Take a corner if free
    move = cornerMove(board)
    if move is not False:
        return move

    # Take a side
    return edgeMove(board)
