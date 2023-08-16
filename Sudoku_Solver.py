import copy
from Sudoku_Generator import random_sample


def get_first_space(puzzle):
    for a in range(9):
        for b in range(9):
            if puzzle[a][b] == 0:
                return a, b
    return None


def is_valid(puzzle, guess, row_num, col_num):
    row_values = puzzle[row_num]
    if guess in row_values:
        return False

    col_values = []
    for i in range(9):
        col_values.append(puzzle[i][col_num])
    if guess in col_values:
        return False

    square_row = row_num // 3
    square_col = col_num // 3
    for a in range(3 * square_row, 3 * square_row + 3):
        for b in range(3 * square_col, 3 * square_col + 3):
            if guess == puzzle[a][b]:
                return False

    return True


def solve_sudoku(puzzle):
    backup_puzzle = copy.deepcopy(puzzle)
    space = get_first_space(puzzle)
    if space is None:
        return True
    else:
        for number in range(1, 10):
            if is_valid(backup_puzzle, number, space[0], space[1]):
                backup_puzzle[space[0]][space[1]] = number
                if solve_sudoku(backup_puzzle):
                    puzzle[space[0]][space[1]] = number
                    return True
                # else:
                #     puzzle[space[0]][space[1]] = 0
            # puzzle = backup_puzzle
    return False


def samples(input_string1, replacement):
    result = []
    for i in range(0, len(input_string1) - len(replacement) + 1):
        new_string = input_string1[:i] + replacement + input_string1[i + len(replacement):]
        result.append(new_string)
    return result

if __name__ == '__main__':
    print("Welcome to Meow Cat's Sudoku Solver.")
    print("Please enter your entire sudoku board as ONE LONG CHAIN of 81 digits.")
    print("The digits should be your board read left to right, top to bottom, starting from the top left.")
    print("Use 0 for empty spots.")
    board = []
    input_string = input("Input your sudoku board here: ")
    # input_string1 = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"

    # for i in range(100):
    #     replace = 25
    #     input_string = random_sample(input_string1, replace)
        # for input_string in samples(input_string1, replacement):
    print(input_string)
    solved_board = []
    for r in range(9):
        row = []
        for c in range(9):
            row.append(int(input_string[r * 9 + c]))
        board.append(copy.deepcopy(row))
    if solve_sudoku(board):
        print("Here is your solved sudoku!")
        for row_number in range(9):
            print(board[row_number])
    else:
        for row_number in range(9):
            print(board[row_number])
        print("Your sudoku is unsolvable.")
        # break
