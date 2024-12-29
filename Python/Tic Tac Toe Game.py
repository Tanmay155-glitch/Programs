board = [' ' for _ in range(9)]  # Tic-Tac-Toe board

def print_board():
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print("--+---+--")

player = 'X'
for _ in range(9):
    print_board()
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
        player = 'O' if player == 'X' else 'X'
    else:
        print("Invalid move, try again.")
print_board()
