import pygame
import random
import time

pygame.init()

WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

def generate_grid():
    return [
        [
            (random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid")

running = True
grid = generate_grid()
last_update = time.time()

while running:
    screen.fill((0, 0, 0))

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(
                screen,
                grid[y][x],
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    pygame.display.flip()

    if time.time() - last_update >= 5:
        grid = generate_grid()
        last_update = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()