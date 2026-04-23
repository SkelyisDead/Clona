import random

import pygame


WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGENERATE_EVENT = pygame.USEREVENT + 1
REGENERATE_INTERVAL_MS = 5000


def generate_color_grid() -> list[list[tuple[int, int, int]]]:
    """Create a new grid filled with random RGB colors."""
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


def draw_color_grid(
    screen: pygame.Surface, color_grid: list[list[tuple[int, int, int]]]
) -> None:
    """Draw the current color grid on the screen."""
    for row_index, row in enumerate(color_grid):
        for column_index, color in enumerate(row):
            rectangle = (
                column_index * CELL_SIZE,
                row_index * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, color, rectangle)


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid")
    color_grid = generate_color_grid()

    # Regenerate the grid automatically every 5 seconds.
    pygame.time.set_timer(REGENERATE_EVENT, REGENERATE_INTERVAL_MS)

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_color_grid(screen, color_grid)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == REGENERATE_EVENT:
                color_grid = generate_color_grid()

    pygame.quit()


if __name__ == "__main__":
    main()