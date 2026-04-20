import pygame
import random
import time


pygame.init()

def generate_color_grid():
    """Generează o matrice 10x10 cu valori RGB aleatoare."""
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]


screen_display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Regenerare la 5 secunde)")


color_matrix = generate_color_grid()
is_running = True


last_update_time = time.time()


while is_running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

  
    current_time = time.time()
    if current_time - last_update_time >= 5:
        color_matrix = generate_color_grid()
        last_update_time = current_time 

  
    screen_display.fill((0, 0, 0)) 

   
    for row in range(10):
        for col in range(10):
           
            x_position = col * 50
            y_position = row * 50
            
           
            current_color = color_matrix[row][col]
            pygame.draw.rect(screen_display, current_color, (x_position, y_position, 50, 50))
            
   
    pygame.display.flip()


pygame.quit()