#...Task...5


board = [' ' for _ in range(9)]

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

def display_board():
    for i in range(0, 9, 3):
        print(f'{board[i]} | {board[i + 1]} | {board[i + 2]}')
        if i < 6:
            print('-' * 9)

def check_win():
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def check_tie():
    return ' ' not in board

current_player = 'X'

while True:
    display_board()
    position = int(input(f"Player {current_player}, enter your position (1-9): ")) - 1

    if board[position] == ' ':
        board[position] = current_player

        if check_win():
            display_board()
            print(f'Player {current_player} wins!')
            break
        elif check_tie():
            display_board()
            print('It\'s a tie!')
            break

        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print('That position is already taken. Try again.')

     
