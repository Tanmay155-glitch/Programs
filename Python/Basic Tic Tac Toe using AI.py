import random

board = [' ' for _ in range(9)]
player = 'X'
ai = 'O'

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(symbol):
    win_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == symbol for a, b, c in win_combos)

while ' ' in board:
    print_board()
    move = int(input("Enter your move (0-8): "))
    if board[move] == ' ':
        board[move] = player
    else:
        print("Invalid move. Try again.")
        continue
    
    if check_winner(player):
        print("Player wins!")
        break

    print("AI is making a move...")
    ai_move = random.choice([i for i in range(9) if board[i] == ' '])
    board[ai_move] = ai
    
    if check_winner(ai):
        print("AI wins!")
        break

print_board()
