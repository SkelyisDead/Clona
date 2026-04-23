import pygame, random
pygame.init()
def generare_culoare():
 return [[(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(10)] for _ in range(10)]
#genereaza o matrice de 10 linii si 10 coloane, care tine minte in fiecare element valorile unei culori RGB

s=pygame.display.set_mode((500,500));
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")
data=generare_culoare();
rulare=True

EVENIMENT_REGEN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENIMENT_REGEN, 5000);

while rulare:
 s.fill((0,0,0)) #un spatiu de a pune culoarea
 for y in range(10):
  for x in range(10): 
    pygame.draw.rect(s,data[y][x],(x*50,y*50,50,50)) #se deseneaza pe templateul s culoarea memorata in data

 pygame.display.flip()

 for e in pygame.event.get():

  if e.type == pygame.QUIT: #verificam daca s-a terminat jocul
    rulare = False

  if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE: # verificam daca se apasa space
    data = generare_culoare()

pygame.quit()