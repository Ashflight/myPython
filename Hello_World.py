import copy
import pygame

list1 = [[1, 2, 3], [4, 5, 6], [7, 8]]

list2 = copy.deepcopy(list1)
list1 = [[0, 1, 2, 3], [4, 5, 6], [7, 8]]
print(list1)
print(list2)

print("Hello World")


def my_function():
    print("Hello from a function")


my_function()


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, color=(255, 0, 0)):
        self.pos = start
        self.color = color

    def draw(self, surface, eyes=False):
        distance = self.w // self.rows
        r = self.pos[0]
        c = self.pos[1]
        pygame.draw.rect(surface, self.color, (r * distance + 1, c * distance + 1, distance - 2, distance - 2))
        if eyes:
            center = distance // 2
            radius = 3
            circle_middle1 = (r * distance - center + radius, c * distance + 8)
            circle_middle2 = (r * distance - distance - radius * 2, c * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle1, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle2, radius)


def draw_grid(w, rows, surface):
    size_between = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


window = pygame.display.set_mode((100, 100))
window.fill((0, 0, 0))
draw_grid(100, 4, window)
pygame.display.update()

snack = cube((2,2), (0, 255, 0))
snack.draw(window)

while True:
    pygame.display.update()
