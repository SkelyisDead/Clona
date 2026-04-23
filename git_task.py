import pygame
import random

pygame.init()

def genereaza_grid_culori():
    grid_nou = []
    for rand in range(10):
        linie_noua = []
        for coloana in range(10):
            rosu = random.randint(0, 255)
            verde = random.randint(0, 255)
            albastru = random.randint(0, 255)
            linie_noua.append((rosu, verde, albastru))
        grid_nou.append(linie_noua)
    return grid_nou

latime_fereastra = 500
inaltime_fereastra = 500
fereastra = pygame.display.set_mode((latime_fereastra, inaltime_fereastra))
pygame.display.set_caption("Grila de Culori Procedurala")

culori_active = genereaza_grid_culori()
este_pornit = True

while este_pornit:
    fereastra.fill((0, 0, 0))
    
    for y in range(10):
        for x in range(10):
            culoare_curenta = culori_active[y][x]
            pozitie_si_dimensiune = (x * 50, y * 50, 50, 50)
            pygame.draw.rect(fereastra, culoare_curenta, pozitie_si_dimensiune)
            
    pygame.display.flip()
    
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            este_pornit = False
        elif eveniment.type == pygame.KEYDOWN:
            if eveniment.key == pygame.K_SPACE:
                culori_active = genereaza_grid_culori()

pygame.quit()