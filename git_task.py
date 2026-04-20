import pygame
import random

# Constants
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
WINDOW_TITLE = "Procedural Color Grid (Press SPACE to Regenerate)"
REGENERATE_INTERVAL = 5000  # 5 seconds in milliseconds


def generate_grid():
    """Generate a 10x10 grid of random RGB colors."""
    return [
        [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(surface, grid):
    """Draw the color grid onto the given surface."""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, grid[y][x], rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(WINDOW_TITLE)

    grid = generate_grid()
    running = True

    # Set a timer to fire every 5 seconds
    pygame.time.set_timer(pygame.USEREVENT, REGENERATE_INTERVAL)

    while running:
        screen.fill((0, 0, 0))
        draw_grid(screen, grid)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                grid = generate_grid()
            elif event.type == pygame.USEREVENT:
                grid = generate_grid()

    pygame.quit()


if __name__ == "__main__":
    main()