import pygame
import random

# Initialize
pygame.init()

# Function to generate a random 10x10 list of colors
def generate_colors():
 return [[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(10)] for _ in range(10)]

# Screen setup
screen = pygame.display.set_mode((500,500))
# Screen title
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
# First generation of array of colors
color_data = generate_colors()
is_running = True

while is_running:
  screen.fill((0,0,0))
  # Draws a square
  for y in range(10):
    for x in range(10):
      color = color_data[y][x]
      pygame.draw.rect(screen, color, (x * 50, y * 50, 50, 50))

  pygame.display.flip()
  # Regenerate every 5 seconds
  pygame.time.delay(5000)
 
  # Event listener for quit and regenerate colors
  for event in pygame.event.get():
    if event.type==pygame.QUIT: 
      is_running=False
    if event.key==pygame.K_SPACE:
      data=generate_colors()

pygame.quit()