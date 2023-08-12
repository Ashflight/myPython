import random
import re


class Board:
    def __init__(self, dimensions, bombs):
        self.dimensions = dimensions
        self.bombs = bombs
        self.dug = set()
        self.board = self.generate_board()
        self.assign_values()

    def generate_board(self):
        board = [[None for a in range(self.dimensions)] for a in range(self.dimensions)]
        bombs_planted = 0
        while bombs_planted < self.bombs:
            location = random.randint(0, self.dimensions**2 - 1)
            row = location // self.dimensions
            col = location % self.dimensions
            if board[row][col] == "*":
                continue
            else:
                board[row][col] = "*"
                bombs_planted += 1
        return board

    def assign_values(self):
        for r in range(self.dimensions):
            for c in range(self.dimensions):
                if self.board[r][c] == "*":
                    continue
                else:
                    self.board[r][c] = self.check_location(r, c)

    def check_location(self, row, col):
        neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dimensions-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dimensions-1, col+1)+1):
                if r == row and c == col:
                    continue
                elif self.board[r][c] == "*":
                    neighboring_bombs += 1
        return neighboring_bombs

    def get_visible_board(self):
        visible_board = [[None for a in range(self.dimensions)] for a in range(self.dimensions)]
        for row in range(0, self.dimensions):
            for col in range(0, self.dimensions):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
        return visible_board

    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True
        else:
            for r in range(max(0, row - 1), min(self.dimensions - 1, row + 1) + 1):
                for c in range(max(0, col - 1), min(self.dimensions - 1, col + 1) + 1):
                    if (r, c) in self.dug:
                        continue
                    else:
                        self.dig(r, c)
        return True

    def mark(self, board, r, c):
        if board[r][c] == " ":
            board[r][c] = "X"
        else:
            print("Invalid move, try again.")
        return board
    # fix bug where Xs don't stay after multiple turns. Need to put X on full board.

    def print_board(self, board):
        for item_row in board:
            print(item_row)


def play(dimensions, bombs):
    board = Board(dimensions, bombs)
    visible_board = board.get_visible_board()
    safe = True
    while len(board.dug) < board.dimensions**2 - bombs:
        board.print_board(visible_board)
        print("Where would you like to dig?")
        print("Please input as \"row, column\". Input a X between the two coordinates if you wish to mark a block.")
        move = re.split(',(\\s)*', input("Input your move here: "))
        row = int(move[0])
        col = int(move[-1])
        if row < 0 or row >= board.dimensions or col < 0 or col >= board.dimensions:
            print("Invalid move, try again.")
            continue
        elif "X" in move:
            board.mark(visible_board, row, col)
        else:
            safe = board.dig(row, col)
            visible_board = board.get_visible_board()
        if not safe:
            break
    if safe:
        board.print_board(board.board)
        print("You won!")
    else:
        print("You lost.")
        board.dug = [(r, c) for r in range(board.dimensions) for c in range(board.dimensions)]
        visible_board = board.get_visible_board()
        board.print_board(visible_board)


if __name__ == '__main__':
    print("Welcome to MineCreeper!")
    d = int(input("Input the dimensions for your (square) mine: "))
    b = int(input("Enter the number of creepers for this round: "))
    play(d, b)
