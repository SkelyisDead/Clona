import pygame
import random
import sys
import time

GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
REFRESH_INTERVAL_SECONDS = 5
BACKGROUND_COLOR = (0, 0, 0)

def generate_random_color():
    """Return a single random RGB color tuple."""
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

def generate_color_grid(width, height):
    """Return a 2D list of random colors for the grid."""
    return [
        [generate_random_color() for _ in range(width)]
        for _ in range(height)
    ]

def draw_color_grid(surface, color_grid):
    """Draw the color grid onto the given pygame surface."""
    for row_index, row in enumerate(color_grid):
        for column_index, color in enumerate(row):
            rectangle = pygame.Rect(
                column_index * CELL_SIZE,
                row_index * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(surface, color, rectangle)

def main():
    """Run the main application loop."""
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(
        "Procedural Color Grid (refresh every 5 seconds)"
    )

    color_grid = generate_color_grid(GRID_SIZE, GRID_SIZE)
    last_refresh_time = time.time()
    running = True

    while running:
        current_time = time.time()
        if current_time - last_refresh_time >= REFRESH_INTERVAL_SECONDS:
            color_grid = generate_color_grid(GRID_SIZE, GRID_SIZE)
            last_refresh_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill(BACKGROUND_COLOR)
        draw_color_grid(display_surface, color_grid)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
