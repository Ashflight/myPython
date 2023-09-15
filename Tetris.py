import pygame
import random

pygame.font.init()

s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(self.shape)]
        self.rotation = 0


def create_grid(locked_positions=None):
    if locked_positions is None:
        locked_positions = {}
    grid = [[(0, 0, 0) for i in range(10)] for i in range(20)]
    for l in range(len(grid)):
        for j in range(len(grid[l])):
            if (j, l) in locked_positions:
                c = locked_positions[(j, l)]
                grid[l][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    shape_format = shape.shape[shape.rotation % len(shape.shape)]
    for l, line in enumerate(shape_format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((shape.x + j, shape.y + l))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y
    for l in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + l * block_size), (sx + play_width, sy + l * block_size))
        for j in range(len(grid[l])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy),
                             (sx + j * block_size, sy + play_height))


def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda a: a[1])[::-1]:
            x, y = key
            if y < ind:
                new_key = (x, y + inc)
                locked[new_key] = locked.pop(key)
    return inc


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255, 255, 255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    formatted = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(formatted):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)
    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface, grid, score=0):
    surface.fill((0, 0, 0))
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 60)
    label = font.render("Tetris", 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Score: " + str(score), 1, (255, 255, 255))
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    surface.blit(label, (sx + 20, sy + 160))
    for l in range(len(grid)):
        for j in range(len(grid[l])):
            pygame.draw.rect(surface, grid[l][j],
                             (top_left_x + j * block_size, top_left_y + l * block_size, block_size, block_size), 0)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)
    draw_grid(surface, grid)


def check_loss(locked_positions, run, surface):
    if check_lost(locked_positions):
        draw_text_middle(surface, "You lost!", 80, (255, 255, 255))
        pygame.display.update()
        pygame.time.delay(3000)
        run = False
    return run


def check_change_piece(change_piece, current_piece, grid, locked_positions, next_piece, score, shape_pos):
    if change_piece:
        for pos in shape_pos:
            p = (pos[0], pos[1])
            locked_positions[p] = current_piece.color
        current_piece = next_piece
        next_piece = get_shape()
        change_piece = False
        score_inc = clear_rows(grid, locked_positions)
        score += score_inc * 10
    return change_piece, current_piece, next_piece, score


def manage_events(current_piece, grid, run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.x -= 1
                if not (valid_space(current_piece, grid)):
                    current_piece.x += 1
            elif event.key == pygame.K_RIGHT:
                current_piece.x += 1
                if not (valid_space(current_piece, grid)):
                    current_piece.x -= 1
            elif event.key == pygame.K_UP:
                current_piece.rotation += 1
                if not (valid_space(current_piece, grid)):
                    current_piece.rotation -= 1
            elif event.key == pygame.K_DOWN:
                current_piece.y += 1
                if not (valid_space(current_piece, grid)):
                    current_piece.y -= 1
    return run


def check_fall(change_piece, current_piece, fall_speed, fall_time, grid, level_speed, level_time):
    if fall_time / 1000 > fall_speed:
        fall_time = 0
        current_piece.y += 1
        if not (valid_space(current_piece, grid)) and current_piece.y > 0:
            current_piece.y -= 1
            change_piece = True
    if level_time / 1000 > level_speed:
        level_time = 0
        if fall_speed > 0.1:
            fall_speed -= 0.005
    return change_piece, fall_time, level_time


def main(surface):
    locked_positions = {}
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3
    level_time = 0
    level_speed = 5
    score = 0
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        change_piece, fall_time, level_time = check_fall(change_piece, current_piece, fall_speed, fall_time, grid, level_speed, level_time)
        run = manage_events(current_piece, grid, run)
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        change_piece, current_piece, next_piece, score = check_change_piece(change_piece, current_piece, grid, locked_positions, next_piece, score, shape_pos)
        draw_window(surface, grid, score)
        draw_next_shape(next_piece, surface)
        pygame.display.update()
        run = check_loss(locked_positions, run, surface)


def main_menu(surface):
    run = True
    while run:
        surface.fill((0, 0, 0))
        draw_text_middle(surface, "Press any key to play!", 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                main(surface)
    pygame.display.quit()


if __name__ == '__main__':
    window = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption("Tetris")
    main_menu(window)
