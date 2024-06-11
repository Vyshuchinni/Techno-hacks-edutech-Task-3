import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != ' ' for row in board for cell in row])

def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column: 1 1 for top-left): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter row and column numbers.")
            continue
        try:
            row, col = int(move[0]) - 1, int(move[1]) - 1
        except ValueError:
            print("Invalid input. Please enter numeric row and column numbers.")
            continue
        if row not in range(3) or col not in range(3):
            print("Invalid move. Please enter numbers between 1 and 3.")
            continue
        if board[row][col] != ' ':
            print("Cell already taken. Choose another cell.")
            continue
        return row, col

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
