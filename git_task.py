import pygame,random

pygame.init()
def creat_matix_of_color():
 return [[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(10)] for _ in range(10)]

#Creaza fereastrra si creaza titlul
window=pygame.display.set_mode((500,500));pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)");
data=creat_matix_of_color();
start=True

while start:
 window.fill((0,0,0))
 for y in range(10):
  for x in range(10):pygame.draw.rect(window,data[y][x],(x*50,y*50,50,50))
 pygame.display.flip()
 
 for event in pygame.event.get():
  start=False if event.type==pygame.QUIT else start;
  data=creat_matix_of_color() if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE else data
pygame.quit()