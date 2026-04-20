import pygame, random, time

#Initializarea jocului
pygame.init()

def generate_grid_data():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for i in range(10)]
            for j in range(10)]

#setarea window-ului
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid")

grid_data = generate_grid_data()
last_update_time = time.time()
is_running = True

while is_running:
    screen.fill((0, 0, 0))
    
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(screen, grid_data[y][x], (x * 50, y * 50, 50, 50))
    
    pygame.display.flip()

    #regenerare la 5 secunde
    if time.time() - last_update_time >= 5:
        grid_data = generate_grid_data()
        last_update_time = time.time()

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            grid_data = generate_grid_data()
            last_update_time = time.time()

#sfarsit program
pygame.quit()