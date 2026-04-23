import pygame
import random
import time
timp_initial=time.time()
pygame.init()
def f():
 g=[]
 for x in range (10):
  l=[]
  for y in range(10):
   c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
   l.append(c)
  g.append(l)
 return g
################################
s=pygame.display.set_mode((500,500));
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)");
data=f();
r=True
while r:
 s.fill((0,0,0))
 for y in range(10):
  for x in range(10):
   pygame.draw.rect(s,data[y][x],(x*50,y*50,50,50))
 pygame.display.flip()

 timp_curent=time.time()
 if timp_curent-timp_initial >=5:
  timp_initial=time.time()
  data=f()

 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   r=False
  elif e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE :
   timp_initial=time.time()
   data=f()
pygame.quit()