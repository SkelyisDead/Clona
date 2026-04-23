import pygame
import random

# Inițializarea motorului Pygame
pygame.init()

def genereaza_matrice_culori(randuri, coloane):
    """
    Generează o matrice de culori RGB aleatorii.
    """
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(coloane)] for _ in range(randuri)]

# Configurații constante (nume sugestive)
LATIME_ECRAN = 500
INALTIME_ECRAN = 500
DIMENSIUNE_CELULA = 50
NR_RANDURI = 10
NR_COLOANE = 10
INTERVAL_REGENERARE = 5000  # 5 secunde exprimate în milisecunde

# Setări fereastră
ecran = pygame.display.set_mode((LATIME_ECRAN, INALTIME_ECRAN))
pygame.display.set_caption("Grilă de Culori Procedurală (Auto-regenerare la 5s)")

# Starea inițială
date_culori = genereaza_matrice_culori(NR_RANDURI, NR_COLOANE)
ruleaza = True
ultimul_timp_actualizare = pygame.time.get_ticks()

# Bucla principală a programului
while ruleaza:
    timp_curent = pygame.time.get_ticks()

    # Verificăm dacă au trecut 5 secunde pentru a regenera culorile
    if timp_curent - ultimul_timp_actualizare >= INTERVAL_REGENERARE:
        date_culori = genereaza_matrice_culori(NR_RANDURI, NR_COLOANE)
        ultimul_timp_actualizare = timp_curent
        print("Culorile au fost regenerate automat!")

    # Desenarea fundalului
    ecran.fill((0, 0, 0))

    # Desenarea grilei (folosim indentare și spațiere corespunzătoare)
    for y in range(NR_RANDURI):
        for x in range(NR_COLOANE):
            culoare = date_culori[y][x]
            patrat = (x * DIMENSIUNE_CELULA, y * DIMENSIUNE_CELULA, DIMENSIUNE_CELULA, DIMENSIUNE_CELULA)
            pygame.draw.rect(ecran, culoare, patrat)

    pygame.display.flip()

    # Gestionarea evenimentelor
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            ruleaza = False
        
        # Regenerare manuală la apăsarea tastei SPACE
        if eveniment.type == pygame.KEYDOWN and eveniment.key == pygame.K_SPACE:
            date_culori = genereaza_matrice_culori(NR_RANDURI, NR_COLOANE)
            ultimul_timp_actualizare = timp_curent

pygame.quit()
