import pygame
import random

# 1. Inițializăm modulul pygame
pygame.init()

def genereaza_matrice_culori():
    """
    Generează o matrice 10x10 cu culori RGB aleatoare.
    Fiecare element din matrice este un tuplu (R, G, B).
    """
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
             for _ in range(10)] for _ in range(10)]

# 2. Setăm dimensiunile ferestrei și titlul (Nume de variabile sugestive)
ecran = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural Color Grid (Regenerare la 5 secunde)")

# 3. Inițializăm variabilele principale
matrice_culori = genereaza_matrice_culori()
program_ruleaza = True

# Salvăm timpul la care s-a generat ultima dată matricea (în milisecunde)
timp_ultima_regenerare = pygame.time.get_ticks()

# Bucla principală a programului
while program_ruleaza:
    # Colorăm fundalul în negru (Spațiere corectă între argumente)
    ecran.fill((0, 0, 0))
    
    # Desenăm grila de 10x10 pe ecran (Indentare corectă de 4 spații)
    for y in range(10):
        for x in range(10):
            culoare_curenta = matrice_culori[y][x]
            # Calculăm poziția x și y înmulțind indexul cu 50 (lățimea/înălțimea unui pătrat)
            pygame.draw.rect(ecran, culoare_curenta, (x * 50, y * 50, 50, 50))
            
    # Actualizăm conținutul afișat pe ecran
    pygame.display.flip()
    
    # 4. Gestionarea evenimentelor (ex: apăsarea butonului X pentru închidere)
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            program_ruleaza = False
            
    # 5. Logica de regenerare a rezultatului o dată la 5 secunde (5000 ms)
    timp_curent = pygame.time.get_ticks()
    
    if timp_curent - timp_ultima_regenerare >= 5000:
        matrice_culori = genereaza_matrice_culori()
        timp_ultima_regenerare = timp_curent

# Închidem aplicația curat după ce ieșim din buclă
pygame.quit()