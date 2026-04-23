import pygame
import random
import time

# Constante
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE


def generate_color_grid():
    """
    Generează o matrice GRID_SIZE x GRID_SIZE
    cu culori random (RGB).
    """
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(screen, color_grid):
    """
    Desenează grila de culori pe ecran.
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = color_grid[row][col]
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid")

    running = True
    color_grid = generate_color_grid()

    last_update_time = time.time()

    while running:
        screen.fill((0, 0, 0))

        # Desenare grid
        draw_grid(screen, color_grid)

        pygame.display.flip()

        # Evenimente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Regenerare automata la fiecare 5 secunde
        current_time = time.time()
        if current_time - last_update_time >= 5:
            color_grid = generate_color_grid()
            last_update_time = current_time

    pygame.quit()


if __name__ == "__main__":
    main()