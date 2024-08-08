def winning_line(strings):
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings

def row_winner(board):
    return any(winning_line(row) for row in board)

def column_winner(board):
    return row_winner(zip(*board))

def main_diagonal_winner(board):
    return winning_line(row[i] for i, row in enumerate(board))

def diagonal_winner(board):
    return main_diagonal_winner(board) or main_diagonal_winner(reversed(board))

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def format_board(board):
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'

def play_move(board, player):
    print(f'{player} to play:')
    row = int(input('Choose a row. ')) - 1
    col = int(input('Choose a column. ')) - 1
    board[row][col] = player
    print(format_board(board))

def make_board(size):
    return [[' '] * size for _ in range(size)]

def print_winner(player):
    print(f'{player} wins!')

def print_draw():
    print("It's a draw!")

def play_game(board_size, player1, player2):
    board = make_board(board_size)
    print(format_board(board))
    total_moves = board_size * board_size
    current_player = player1
    for i in range(total_moves):
        play_move(board, current_player)
        if winner(board):
            print_winner(current_player)
            return
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    print_draw()
        
board_s = int(input('What board size do you want? '))
p1_char = input(f'What letter is player 1? ')
while len(p1_char) > 1:
    p1_char = input('Please enter one character only. ')
while p1_char.isnumeric == True:
    p1_char = input('Please enter characters only. ')
p2_char = input(f'What letter is player 2? ')
while len(p2_char) > 1:
    p2_char = input('Please enter one character only. ')
while p2_char.isnumeric == True:
    p2_char = input('Please enter characters only. ')

play_game(board_s, p1_char, p2_char)
