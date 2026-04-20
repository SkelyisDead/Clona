import pygame
import random
import time

# Inițializăm modulul pygame
pygame.init()

# Funcție cu nume sugestiv pentru a genera grila de culori
def genereaza_matrice_culori():
    # Generăm o matrice 10x10 cu valori RGB (Red, Green, Blue) aleatoare
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(10)] for _ in range(10)]

# Setăm dimensiunile ferestrei și o salvăm într-o variabilă clară
latime_fereastra = 500
inaltime_fereastra = 500
ecran_joc = pygame.display.set_mode((latime_fereastra, inaltime_fereastra))

pygame.display.set_caption("Procedural Color Grid (Regenerare la 5 secunde)")

# Variabile inițiale pentru starea programului
matrice_culori = genereaza_matrice_culori()
ruleaza_programul = True
timp_ultima_regenerare = time.time()

# Bucla principală a programului
while ruleaza_programul:
    # Curățăm ecranul cu negru
    ecran_joc.fill((0, 0, 0))
    
    # Desenăm dreptunghiurile colorate pe ecran, respectând indentarea și spațierea
    for y in range(10):
        for x in range(10):
            pygame.draw.rect(ecran_joc, matrice_culori[y][x], (x * 50, y * 50, 50, 50))
            
    pygame.display.flip()
    
    # Task: Programul să regenereze rezultatul o dată la 5 secunde
    timp_curent = time.time()
    if timp_curent - timp_ultima_regenerare >= 5.0:
        matrice_culori = genereaza_matrice_culori()
        timp_ultima_regenerare = timp_curent # Resetăm timer-ul
        
    # Verificăm evenimentele (ex: închiderea ferestrei sau apăsarea tastei SPACE)
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            ruleaza_programul = False
            
        # Păstrăm și funcționalitatea originală: regenerare manuală la apăsarea tastei SPACE
        if eveniment.type == pygame.KEYDOWN and eveniment.key == pygame.K_SPACE:
            matrice_culori = genereaza_matrice_culori()
            timp_ultima_regenerare = time.time() # Resetăm timer-ul și aici

pygame.quit()