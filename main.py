import pygame
import sys

SIZE_BLOCK = (20)
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
COUNT_BLOCKS = 20
MARGIN = 1
HEADER_MARGIN = 70
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)

size = (SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer = pygame.time.Clock()


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def is_inside(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y <SIZE_BLOCK


def draw_block(color, row, column):
    pygame.draw.rect(screen, color, (
        SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
        HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK,
        SIZE_BLOCK))


snake_block = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]

d_row = 0
d_col = 1

while True:  # Что бы окно не закрывалось

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1
    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color, row, column)

    head = snake_block[-1]
    if not head.is_inside():
        pygame.quit()
        sys.exit()
    for block in snake_block:
        draw_block(SNAKE_COLOR, block.x, block.y)

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_block.append(new_head)
    snake_block.pop(0)

    pygame.display.flip()
    timer.tick(2)
