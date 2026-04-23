import pygame
import random

GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
REGENERATE_INTERVAL_MS = 5000
REGENERATE_EVENT = pygame.USEREVENT + 1


def generate_grid_colors(size):
  return [
    [
      (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      for _ in range(size)
    ]
    for _ in range(size)
  ]


def draw_grid(screen, colors, cell_size):
  for row_index, row_colors in enumerate(colors):
    for col_index, color in enumerate(row_colors):
      pygame.draw.rect(
        screen,
        color,
        (col_index * cell_size, row_index * cell_size, cell_size, cell_size),
      )


def main():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
  pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
  pygame.time.set_timer(REGENERATE_EVENT, REGENERATE_INTERVAL_MS)

  colors = generate_grid_colors(GRID_SIZE)
  running = True
  clock = pygame.time.Clock()

  while running:
    screen.fill((0, 0, 0))
    draw_grid(screen, colors, CELL_SIZE)
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == REGENERATE_EVENT:
        colors = generate_grid_colors(GRID_SIZE)
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        colors = generate_grid_colors(GRID_SIZE)

    clock.tick(60)

  pygame.quit()


if __name__ == "__main__":
  main()