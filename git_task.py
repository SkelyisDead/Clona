import random

import pygame


GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
REGENERATE_INTERVAL_MS = 5000
BACKGROUND_COLOR = (0, 0, 0)


def generate_color_grid():
    """Create a grid filled with random RGB colors."""
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


def draw_color_grid(screen, color_grid):
    """Draw the current color grid on the screen."""
    screen.fill(BACKGROUND_COLOR)

    for row_index in range(GRID_SIZE):
        for column_index in range(GRID_SIZE):
            rectangle = (
                column_index * CELL_SIZE,
                row_index * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, color_grid[row_index][column_index], rectangle)


def main():
    """Run the procedural color grid application."""
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid")
    clock = pygame.time.Clock()

    color_grid = generate_color_grid()
    last_regeneration_time = pygame.time.get_ticks()
    is_running = True

    while is_running:
        current_time = pygame.time.get_ticks()
        if current_time - last_regeneration_time >= REGENERATE_INTERVAL_MS:
            color_grid = generate_color_grid()
            last_regeneration_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Allow manual regeneration in addition to the automatic refresh.
                color_grid = generate_color_grid()
                last_regeneration_time = current_time

        draw_color_grid(screen, color_grid)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()