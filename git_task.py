import pygame
import random

# Initializam libraria Pygame
pygame.init()

def genereaza_grila_culori():
    # Generam o matrice de 10x10 cu culori RGB (Red, Green, Blue) aleatorii
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)] for _ in range(10)]

# Setam dimensiunea ferestrei si titlul (modificat pentru a reflecta timerul)
fereastra = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Grila Culori Procedurala (Auto-Regenerare la 5 secunde)")

# Generam datele initiale si setam starea programului
grila_culori = genereaza_grila_culori()
ruleaza = True

# Cream un Timer in Pygame care va emite un semnal la fiecare 5000 de milisecunde (5 secunde)
EVENIMENT_REGENERARE = pygame.USEREVENT + 1
pygame.time.set_timer(EVENIMENT_REGENERARE, 5000)

# Bucla principala a programului
while ruleaza:
    # Curatam fundalul ferestrei cu negru
    fereastra.fill((0, 0, 0))
    
    # Parcurgem matricea si desenam cate un patrat colorat pentru fiecare element
    for coordonata_y in range(10):
        for coordonata_x in range(10):
            culoare_curenta = grila_culori[coordonata_y][coordonata_x]
            # Desenam dreptunghiul la coordonatele x, y cu dimensiunea de 50x50 pixeli
            pygame.draw.rect(fereastra, culoare_curenta, (coordonata_x * 50, coordonata_y * 50, 50, 50))
            
    # Actualizam imaginea de pe ecran
    pygame.display.flip()
    
    # Verificam ce evenimente se intampla
    for eveniment in pygame.event.get():
        # Daca utilizatorul apasa X pentru a inchide fereastra
        if eveniment.type == pygame.QUIT:
            ruleaza = False
            
        # Daca s-au scurs cele 5 secunde (Timer-ul nostru a declansat evenimentul)
        if eveniment.type == EVENIMENT_REGENERARE:
            grila_culori = genereaza_grila_culori()

# Inchidem programul corect si eliberam memoria
pygame.quit() 