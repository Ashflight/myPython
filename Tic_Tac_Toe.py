import random
import copy

board = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
]

def print_board(board_list):
    for item in board_list:
        print(item)

def update(move, player, game_board):
    game_board[move//3][move%3] = player

def update2(row, col, player, game_board):
    game_board[row][col] = player

def get_available_moves(game_board):
    available_moves = []
    for row in game_board:
        for spot in row:
            if spot != "O" and spot != "X":
                available_moves.append(spot)
    return available_moves

def random_computer_move(game_board):
    available_moves = get_available_moves(game_board)
    move = randomize_move(available_moves)
    update(move, "O", game_board)

def randomize_move(available_moves):
    if 4 in available_moves:
        return 4
    else:
        even_available = []
        for item in available_moves:
            if item%2 == 0:
                even_available.append(item)
        if even_available:
            return random.choice(even_available)
        else:
            return random.choice(available_moves)

def smart_computer_move(game_board):
    available_moves = get_available_moves(game_board)
    find_next_move = test_move(available_moves, game_board, "O")
    if not find_next_move:
        find_next_move = test_move(available_moves, game_board, "X")
    if not find_next_move:
        random_computer_move(game_board)
    print("The computer has moved.")
    print_board(game_board)

def test_move(available_moves, game_board, player):
    find_next_move = False
    for move in available_moves:
        current_board = copy.deepcopy(game_board)
        update(move, player, current_board)
        if check_win(player, current_board):
            update(move, "O", game_board)
            find_next_move = True
            break
    return find_next_move

def find_win_combinations(game_board):
    win_combinations = []

    for item in game_board:
        win_combinations.append(item)

    for number in range(0, 3):
        column = []
        for item in game_board:
            column.append(item[number])
        win_combinations.append(column)

    diagonal1 = [game_board[0][0], game_board[1][1], game_board[2][2]]
    diagonal2 = [game_board[0][2], game_board[1][1], game_board[2][0]]
    win_combinations.extend([diagonal1, diagonal2])

    return win_combinations

def check_win(player, game_board):
    all_combinations = find_win_combinations(game_board)
    for item in all_combinations:
        player_occurrence = item.count(player)
        if player_occurrence == 3:
            return True
    return False

def user_move(game_board):
    user_input = int(input("Enter the corresponding number of the square you wish to move to: "))
    update(user_input, "X", game_board)
    print_board(game_board)

if __name__ == '__main__':
    print_board(board)
    while True:
        user_move(board)
        if check_win("X", board):
            print("You win!")
            break
        empty_spots = get_available_moves(board)
        if not empty_spots:
            print("The game ends in a tie.")
            break
        # random_computer_move(board)
        smart_computer_move(board)
        if check_win("O", board):
            print("You lose.")
            break