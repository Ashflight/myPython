import copy
import random


def random_sample(board, spaces):
    board_list = []
    for character in range(len(board)):
        board_list.append(board[character])

    spaces_added = 0
    while spaces_added < spaces:
        location = random.randrange(0, 81, 1)
        if board_list[location] != 0:
            board_list[location] = 0
            spaces_added += 1

    board = ""
    for item in range(len(board_list)):
        board = board + str(board_list[item])

    return board

if __name__ == '__main__':
    board = input("Input board here: ")
    spaces = int(input("Input the number of spaces to generate: "))

    board_list = random_sample(board, spaces)
    board_2d_list = []
    for r in range(9):
        row = []
        for c in range(9):
            row.append(int(board_list[r * 9 + c]))
        board_2d_list.append(copy.deepcopy(row))

    for number in range(9):
        print(board_2d_list[number])

