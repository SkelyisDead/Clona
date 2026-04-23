import random
import pygame

pygame.init()

GRID_SIZE = 10
WINDOW_SIZE = 500
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
AUTO_REGENERATE_INTERVAL_MS = 5000

def generate_color_grid():
  """Genereaza matrice RGB"""
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

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

grid_data = generate_color_grid()
running = True
last_regeneration_time = pygame.time.get_ticks()

while running:
  screen.fill((0, 0, 0))

  for row_index in range(GRID_SIZE):
    for col_index in range(GRID_SIZE):
      pygame.draw.rect(
        screen,
        grid_data[row_index][col_index],
        (col_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE),
      )

  pygame.display.flip()

  current_time = pygame.time.get_ticks()
  if current_time - last_regeneration_time >= AUTO_REGENERATE_INTERVAL_MS:
    grid_data = generate_color_grid()
    last_regeneration_time = current_time

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      grid_data = generate_color_grid()
      last_regeneration_time = pygame.time.get_ticks()

pygame.quit()