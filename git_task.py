import pygame
import random


LATIME_FEREASTRA = 500
INALTIME_FEREASTRA = 500
DIMENSIUNE_CELULA = 50
NUMAR_RANDURI = 10
NUMAR_COLOANE = 10
INTERVAL_REGENERARE_MS = 5000  

def genereaza_matrice_culori():
    """
    Generează o matrice de 10x10 conținând culori RGB aleatorii.
    Returnează o listă de liste de tupluri (R, G, B).
    """
    matrice = []
    for _ in range(NUMAR_RANDURI):
        rand_culori = []
        for _ in range(NUMAR_COLOANE):
            
            culoare_aleatorie = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            rand_culori.append(culoare_aleatorie)
            
        matrice.append(rand_culori)
        
    return matrice

def ruleaza_aplicatia():
    """
    Inițializează fereastra Pygame și rulează bucla principală.
    Aici se gestionează desenarea și actualizarea la fiecare 5 secunde.
    """
    pygame.init()
    
    fereastra = pygame.display.set_mode((LATIME_FEREASTRA, INALTIME_FEREASTRA))
    pygame.display.set_caption("Grid Culori (Regenerare la 5 secunde)")
    
    
    grid_culori = genereaza_matrice_culori()
    ruleaza = True
    
    timp_ultima_regenerare = pygame.time.get_ticks()

    while ruleaza:
        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:
                ruleaza = False
                
        timp_curent = pygame.time.get_ticks()
        if timp_curent - timp_ultima_regenerare >= INTERVAL_REGENERARE_MS:
            grid_culori = genereaza_matrice_culori()
            timp_ultima_regenerare = timp_curent     

        fereastra.fill((0, 0, 0))  
        
        for y in range(NUMAR_RANDURI):
            for x in range(NUMAR_COLOANE):
                culoare_curenta = grid_culori[y][x]
                coordonata_x = x * DIMENSIUNE_CELULA
                coordonata_y = y * DIMENSIUNE_CELULA

                pygame.draw.rect(
                    fereastra, 
                    culoare_curenta, 
                    (coordonata_x, coordonata_y, DIMENSIUNE_CELULA, DIMENSIUNE_CELULA)
                )

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    ruleaza_aplicatia()