import math

board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in pos) for pos in win_positions)

def is_draw():
    return ' ' not in board

def minimax(is_max):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

print("TIC TAC TOE - YOU (X) vs AI (O)")
print_board()

while True:
    move = int(input("Enter your move (0-8): "))
    if board[move] != ' ':
        print("Invalid move!")
        continue

    board[move] = 'X'
    print_board()

    if check_winner('X'):
        print("You win!")
        break
    if is_draw():
        print("It's a draw!")
        break

    ai_move = best_move()
    board[ai_move] = 'O'
    print("AI move:")
    print_board()

    if check_winner('O'):
        print("AI wins!")
        break
