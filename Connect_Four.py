import pygame
import tkinter as tk
from tkinter import messagebox
import keyboard


class Stone:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, surface):
        center = (self.position[0] * 50 + 25, self.position[1] * 50 + 25)
        pygame.draw.circle(surface, self.color, center, 25)


def check(location1, location2, location3, location_list, color):
    if location1 in location_list and location2 in location_list and location3 in location_list:
        if color == (255, 0, 0):
            message_box("Red wins!", "The game has finished with red winning.")
        else:
            message_box("Yellow wins!", "The game has finished with yellow winning.")


def on_key_event(e):
    global stones, valid_move
    valid_move = True
    if e.event_type == keyboard.KEY_UP and e.name == "left":
        new_stone = stones[-1]
        new_stone.position = (max(new_stone.position[0] - 1, 0), new_stone.position[1])
    elif e.event_type == keyboard.KEY_UP and e.name == "right":
        new_stone = stones[-1]
        new_stone.position = (min(new_stone.position[0] + 1, 6), new_stone.position[1])
    elif e.event_type == keyboard.KEY_UP and e.name == "down":
        new_stone = stones[-1]
        row_numbers = []
        for item in stones:
            if item.position[0] == new_stone.position[0]:
                row_numbers.append(item.position[1])
        row_numbers.sort()
        try:
            if row_numbers[1] == 1:
                valid_move = False
            else:
                new_stone.position = (new_stone.position[0], row_numbers[1] - 1)
        except IndexError:
            new_stone.position = (new_stone.position[0], 6)
        stone_positions = []
        for stone in stones:
            if new_stone.color == stone.color:
                stone_positions.append(stone.position)
        for position in stone_positions:
            check((position[0] + 1, position[1]), (position[0] + 2, position[1]), (position[0] + 3, position[1]), stone_positions, new_stone.color)
            check((position[0], position[1] + 1), (position[0], position[1] + 2), (position[0], position[1] + 3), stone_positions, new_stone.color)
            check((position[0] + 1, position[1] + 1), (position[0] + 2, position[1] + 2), (position[0] + 3, position[1] + 3), stone_positions, new_stone.color)
            check((position[0] + 1, position[1] - 1), (position[0] + 2, position[1] - 2), (position[0] + 3, position[1] - 3), stone_positions, new_stone.color)
        if len(stones) >= 42:
            message_box("Tie.", "The game has finished with a tie.")
        if valid_move:
            if new_stone.color == (255, 0, 0):
                generated_stone = Stone((255, 255, 0), (3, 0))
                stones.append(generated_stone)
            else:
                generated_stone = Stone((255, 0, 0), (3, 0))
                stones.append(generated_stone)
    redraw_window(window.get_width(), window, stones)


def draw_board(w, r, surface):
    size_between = w // r
    x = 0
    y = 0
    for l in range(r):
        x += size_between
        y += size_between
        pygame.draw.line(surface, (255, 255, 255), (x, size_between), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(w, surface, stone_list):
    surface.fill((0, 0, 0))
    draw_board(w, 7, surface)
    for number in range(len(stone_list)):
        placed_stone = stone_list[number]
        placed_stone.draw(surface)
    pygame.display.update()


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


global stones, valid_move
width = 350
window = pygame.display.set_mode((width, width))
stones = []
clock = pygame.time.Clock()
first_stone = Stone((255, 255, 0), (3, 0))
stones.append(first_stone)
valid_move = True

keyboard.hook(on_key_event)

while True:
    redraw_window(width, window, stones)
