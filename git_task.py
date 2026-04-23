import pygame
import random

pygame.init()

def generate_color_grid():
  return [
    [
      (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
      )
      for _ in range(10)
    ]
    for _ in range(10)
  ]

# initializare display
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
color_grid = generate_color_grid()
is_running = True
clock = pygame.time.Clock()
last_regenerate = pygame.time.get_ticks()

# game loop
while is_running:
  display.fill((0, 0, 0))

  for y in range(10):
    for x in range(10):
      pygame.draw.rect(
        display,
        color_grid[y][x],
        (x * 50, y * 50, 50, 50)
      )

  # update display
  pygame.display.flip()

  # genereare la 5 sec
  current_time = pygame.time.get_ticks()
  if current_time - last_regenerate >= 5000:
    color_grid = generate_color_grid()
    last_regenerate = current_time

  # events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      color_grid = generate_color_grid()
      last_regenerate = pygame.time.get_ticks()

  clock.tick(60)

pygame.quit()