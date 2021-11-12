import pygame,random
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
groundx=0
speed=0
class Bird:
    bird=pygame.Rect(100,250,30,30)
    
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-5
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    #bpipe=pygame.Rect(250,400,40,320)
    def __init__(self,x):
        # Assign a fixed value to the variable 'self.height' 
        
        self.tpipe=pygame.Rect(x,self.height-400,40,320)
        self.bpipe=pygame.Rect(x,self.height+100,40,500)
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      screen.blit(images["invertedpipe"],self.tpipe)
    def move(self):
        self.tpipe.x-=2
        self.bpipe.x-=2
bird1=Bird()
pipe1=Pipe(150)
pipe2=Pipe(250)
while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-450:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  pipe1.display()
  pipe1.move()
  pipe2.display()
  pipe2.move()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            bird1.moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
