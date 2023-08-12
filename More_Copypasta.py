class Member:

    def __init__(self, name, age, positions, is_male):
        self.name = name
        self.age = age
        self.positions = positions
        self.is_male = is_male

    # You can put functions in classes
    def in_vocal_line(self):
        if "Vocalist" in self.positions:
            return True
        else:
            return False

class NyangDaeng_Unit:

    def make_smoothies(self):
        print("The unit makes smoothies.")

    def make_pancakes(self):
        print("The unit makes pancakes.")

    def make_lollipops(self):
        print("The unit makes lollipops.")

    def kitchen_disaster(self):
        print("The unit failed to make anything edible.")

    def improvise(self):
        print("The unit tries to make cookies.")

all_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`-=[]\;',./~!@#$%^&*()_+{}|:\"<>?"

# This stuff is for tic tac tow

import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[1*3:(i+1)*3] for i in range(3)]:
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

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner[square, letter]:
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
            diagonal_2 = [self.board[1] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_2]):
                return True

        return False

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class Random_Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        value = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return value

class Unbeatable_Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)
        return square['position']

    def minimax(self, game_state, player):
        max_player = self.letter
        min_player = 'o' if player == 'X' else 'X'
        score = 0

        if game_state.winner == min_player:
            if min_player == max_player:
                score = 1 * (game_state.num_empty_squares() + 1)
            else:
                score = -1 * (game_state.num_empty_squares() + 1)
            return {
                'position': None,
                'score': score
            }
        elif not game_state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in game_state.available_moves():
            game_state.make_move(possible_move, player)
            sim_score =self.minimax(game_state, min_player)
            game_state.board[possible_move] = ' '
            game_state.winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best