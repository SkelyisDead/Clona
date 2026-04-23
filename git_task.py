import random

import pygame


WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
BACKGROUND_COLOR = (0, 0, 0)
REGENERATE_INTERVAL_MS = 5000


def generate_color_grid(rows: int, columns: int) -> list[list[tuple[int, int, int]]]:
  """Generate a 2D grid of random RGB colors."""
  return [
    [
      (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
      )
      for _ in range(columns)
    ]
    for _ in range(rows)
  ]


def draw_color_grid(
  surface: pygame.Surface,
  color_grid: list[list[tuple[int, int, int]]],
) -> None:
  """Draw the color grid on the provided surface."""
  for row_index in range(GRID_SIZE):
    for column_index in range(GRID_SIZE):
      cell_color = color_grid[row_index][column_index]
      cell_rect = (
        column_index * CELL_SIZE,
        row_index * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE,
      )
      pygame.draw.rect(surface, cell_color, cell_rect)


def main() -> None:
  """Run the Pygame loop and regenerate colors every 5 seconds."""
  pygame.init()

  screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
  pygame.display.set_caption("Procedural Color Grid")

  color_grid = generate_color_grid(GRID_SIZE, GRID_SIZE)
  last_regeneration_time = pygame.time.get_ticks()
  is_running = True

  while is_running:
    current_time = pygame.time.get_ticks()

    # Regenerate the grid every 5 seconds.
    if current_time - last_regeneration_time >= REGENERATE_INTERVAL_MS:
      color_grid = generate_color_grid(GRID_SIZE, GRID_SIZE)
      last_regeneration_time = current_time

    screen.fill(BACKGROUND_COLOR)
    draw_color_grid(screen, color_grid)
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        is_running = False

      # Optional: keep manual regeneration via SPACE key.
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        color_grid = generate_color_grid(GRID_SIZE, GRID_SIZE)
        last_regeneration_time = current_time

  pygame.quit()


if __name__ == "__main__":
  main()