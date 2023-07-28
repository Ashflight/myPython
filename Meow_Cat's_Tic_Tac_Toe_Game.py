from More_Copypasta import Random_Computer, Human, Unbeatable_Computer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.win(square, letter):
                self.winner = letter
            return True
        return False

    def win(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square ' + str(square) + ".")
                game.print_board()
                print(' ')

            if game.winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            if letter == 'O':
                letter = 'X'
            else:
                letter = 'O'

        time.sleep(1)

    if print_game:
        print('It\'s a tie.')

if __name__ == '__main__':
    x_player = Human('X')
    o_player = Unbeatable_Computer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)