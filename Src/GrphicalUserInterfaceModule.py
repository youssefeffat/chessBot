import matplotlib.pyplot as plt
# import tkinter as tk
from matplotlib.patches import Rectangle

def fen_to_board(fen):
    fen_parts = fen.split()
    piece_placement = fen_parts[0]

    board = []

    for rank in piece_placement.split('/'):
        row = []
        for char in rank:
            if char.isdigit():
                # Add empty squares
                row.extend(['.' for _ in range(int(char))])
            else:
                # Add the piece
                row.append(char)
        board.append(row)

    return board

def display_chessboard(ax,board):
    ax.clear()
    #fig, ax = plt.subplots(figsize=(8, 8))
    colors = ["#F0D9B5", "#006400"]  
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            ax.add_patch(Rectangle((col, 7 - row), 1, 1, color=color))

    piece_symbols = {
        'P': '\u2659', 'N': '\u2658', 'B': '\u2657', 'R': '\u2656', 'Q': '\u2655', 'K': '\u2654',
        'p': '\u265F', 'n': '\u265E', 'b': '\u265D', 'r': '\u265C', 'q': '\u265B', 'k': '\u265A'
    }
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '.':
                ax.text(col + 0.5, 7 - row + 0.5, piece_symbols[piece], fontsize=32, ha='center', va='center', 
                        color="black" if piece.islower() else "#FFFFFF", weight="bold")

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xticks(range(9))
    ax.set_yticks(range(9))
    ax.set_xticklabels([''] + list('abcdefgh'))
    ax.set_yticklabels([''] + list(map(str, range(8, 0, -1))))
    ax.grid(False)
    ax.axis('off')

    #plt.show()


fig,ax=plt.subplots(figsize=(8,8))
# root = tk.Tk()
# canvas = tk.FigureCanvasTkAgg(fig, root)
running = True
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

chess_board = fen_to_board(fen)

display_chessboard(ax,chess_board)
plt.ion()
plt.show()
while running: 
    user_input = input("Enter Fen: ") #Exemple: rnbqkbnr/ppp1pppp/8/3p4/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    if user_input.lower() == 'quit':
        running = False

    else:
        chess_board=fen_to_board(user_input)
        display_chessboard(ax,chess_board)
    print("DEBUG")
    
