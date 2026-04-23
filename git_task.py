import random, pygame

GRID_SIZE = 10
CELL_SIZE = 50
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
REGENERATION_INTERVAL = 5


def generate_color_grid():
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


def draw_color_grid(screen_surface, color_grid):
  for row_index in range(GRID_SIZE):
    for column_index in range(GRID_SIZE):
      pygame.draw.rect(
        screen_surface,
        color_grid[row_index][column_index],
        (
          column_index * CELL_SIZE,
          row_index * CELL_SIZE,
          CELL_SIZE,
          CELL_SIZE,
        ),
      )


pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

color_grid = generate_color_grid()
is_running = True
last_regeneration_time = pygame.time.get_ticks()

while is_running:
  current_time = pygame.time.get_ticks()

  if current_time - last_regeneration_time >= REGENERATION_INTERVAL * 1000:
    color_grid = generate_color_grid()
    last_regeneration_time = current_time

  screen.fill((0, 0, 0))
  draw_color_grid(screen, color_grid)
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      color_grid = generate_color_grid()
      last_regeneration_time = current_time

pygame.quit()
