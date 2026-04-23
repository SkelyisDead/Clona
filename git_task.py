import pygame
import random

# Inițializăm biblioteca Pygame
pygame.init()

# Definim constante pentru a evita "numerele magice" în cod
LATIME_FEREASTRA = 500
INALTIME_FEREASTRA = 500
DIMENSIUNE_CELULA = 50
NUMAR_CELULE = 10
TIMP_REGENERARE_MS = 5000  # 5 secunde = 5000 milisecunde

def genereaza_grila_culori():
    """
    Generează o matrice 10x10, unde fiecare element 
    este un tuplu reprezentând o culoare RGB aleatoare.
    """
    grila = []
    for rand in range(NUMAR_CELULE):
        rand_culori = []
        for coloana in range(NUMAR_CELULE):
            # Generăm culori RGB (Red, Green, Blue) între 0 și 255
            culoare_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            rand_culori.append(culoare_rgb)
        grila.append(rand_culori)
    
    return grila

# Configurăm ecranul principal
ecran = pygame.display.set_mode((LATIME_FEREASTRA, INALTIME_FEREASTRA))
pygame.display.set_caption("Procedural Color Grid (Regenerare automata la 5 secunde)")

# Generăm prima grilă de culori și pornim cronometrul
culori_grila = genereaza_grila_culori()
timp_ultima_actualizare = pygame.time.get_ticks()
program_ruleaza = True

# Bucla principală a ferestrei grafice
while program_ruleaza:
    
    # 1. Desenăm fundalul negru
    ecran.fill((0, 0, 0))
    
    # 2. Desenăm grila de culori
    for index_y in range(NUMAR_CELULE):
        for index_x in range(NUMAR_CELULE):
            culoare_celula = culori_grila[index_y][index_x]
            coordonata_x = index_x * DIMENSIUNE_CELULA
            coordonata_y = index_y * DIMENSIUNE_CELULA
            
            # Parametrii: ecranul, culoarea, (X, Y, Lățime, Înălțime)
            pygame.draw.rect(ecran, culoare_celula, (coordonata_x, coordonata_y, DIMENSIUNE_CELULA, DIMENSIUNE_CELULA))
            
    pygame.display.flip() # Afișăm pe ecran ce am desenat
    
    # 3. Verificăm dacă au trecut 5 secunde pentru a regenera grila
    timp_curent = pygame.time.get_ticks()
    if timp_curent - timp_ultima_actualizare >= TIMP_REGENERARE_MS:
        culori_grila = genereaza_grila_culori()
        timp_ultima_actualizare = timp_curent # Resetăm cronometrul

    # 4. Verificăm evenimentele sistemului (ex: apăsarea butonului X de închidere)
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            program_ruleaza = False

# Închidem programul curat
pygame.quit()