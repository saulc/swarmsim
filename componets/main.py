'''
Created on Feb 13, 2016

@author: saul
'''


import pygame, sys
from componets.bot import Bot


class Menu():
     
    bg = []
    background_image = 0
    eFrames = []
    bgh = 0
    width = 900
    height = 900
    surface = 0
    fullscreen = False
    keys = []
    isPaused = False
    showPath = False
    robots = 0
    
    def __init__(self):
        pygame.init()
        
        if Menu.fullscreen and Menu.width == 0:
            Menu.width = pygame.display.Info().current_w
            Menu.height = pygame.display.Info().current_h
            Menu.surface = pygame.display.set_mode([Menu.width, Menu.height], pygame.FULLSCREEN)
        else:
            Menu.surface = pygame.display.set_mode([Menu.width, Menu.height])
            
        pygame.display.set_caption('Swarm Sim by ACME')
        
        self.setupKeys()
        
       # Menu.background_image =   pygame.image.load("./atksmall.png").convert() 
        #Menu.bg.append(  pygame.image.load("./heartlogo.png").convert_alpha() )

        self.mainMenu() #start

              
        
    def mainMenu(self):
        red = pygame.Color(255, 20, 20)
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        bgColor= pygame.Color(20, 200, 43)
        FPS = 30 #30 frames per second
        fpsClock = pygame.time.Clock()
        
        pygame.font.init()
#         fonts = pygame.font.get_fonts()
#         for f in fonts:
#             print(f)
        text = ['Swarm', 'More Info']
        selected = 1
        
        self.createEframes()
       
        Menu.robots = pygame.sprite.Group()  
        b = Bot(self,self.width/3,100, 3)
        b.setEframe(Menu.eFrames)
        Menu.robots.add(b)
        
        a = Bot(self,self.width/3*2,600, 3)
        a.setEframe(Menu.eFrames)
        Menu.robots.add(a)
        
        c = Bot(self,self.width/2,500, 3)
        c.setEframe(Menu.eFrames)
        Menu.robots.add(c)
        #c.setV(2, 1)
        
        Menu.surface.fill(bgColor)
        pygame.draw.circle(Menu.surface, white, [Menu.width//2, Menu.height//2], 50, 5)
        
        #title
        f = "comicsansms"
        myfont = pygame.font.SysFont(f, 42, True, True)
        label = myfont.render(text[0], True, white)
        Menu.surface.blit(label, (Menu.width//2-39*len(text[0])/2, Menu.height//2-60 ))
            
        Menu.background_image = pygame.Surface.copy(Menu.surface)        #save the parts that dont change
            
        # main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('time to quit')
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #print('key pressed')
                    if event.type == pygame.KEYDOWN:
                        Menu.keys[event.key](True)
                    elif event.type == pygame.KEYUP:
                        Menu.keys[event.key](False)
                 
            if not Menu.showPath:
                Menu.surface.fill(bgColor)
                pygame.draw.circle(Menu.surface, white, [Menu.width//2, Menu.height//2], 50, 5)
        
                #Menu.surface = pygame.Surface.copy(Menu.background_image)
            #Menu.surface.blit(Menu.background_image, [0, Menu.bgh])
            Menu.robots.update()
            Menu.robots.draw(Menu.surface)
        
           # pygame.draw.rect(Menu.surface, red, [120,300, Menu.bg[3].get_width(), Menu.bg[3].get_height()], 5)
            
#             for i in range(1, len(text)):       
#                 myfont = pygame.font.SysFont(f, 85, (i == selected), False)
#                 label = myfont.render(text[i], True, white)
#                 Menu.surface.blit(label, (Menu.width//2-42*len(text[i])/2, 200 + i*120))        #centered
# 
#             
          
            pygame.display.update()
            fpsClock.tick(FPS)
        
    def buttonUp(self, pressed):
        print("Up")
        if pressed:
            for b in Menu.robots:
                b.faster()
        
    def buttonDown(self, pressed):
        print("Down")
        if pressed:
            for b in Menu.robots:
                b.slower()
            
    def buttonLeft(self, pressed):
        print("Left")
        if pressed:
            for b in Menu.robots:
                b.nextMode()
        
                
    def buttonRight(self, pressed):
        print("right")
        if pressed:
            for b in Menu.robots:
                b.prevMode()
        
                
    def buttonSpace(self, pressed):
        print("space")
        
        
    def buttonNothing(self, pressed):
        pass
    
    def boom(self, pressed):
        print("click, click...")
        if pressed:   
            for b in Menu.robots:
                b.bang()
            
        
    def pause(self, pressed):
        if pressed:
            Menu.isPaused = not Menu.isPaused 
    def buttonP(self, pressed):
        if pressed:
            Menu.showPath = not Menu.showPath 
            
    def quit(self, pressed):
        print('time to quit')
        pygame.quit()
        sys.exit()
        
    def setupKeys(self):
        for i in range(512):
            Menu.keys.append(self.buttonNothing)
            
            
        Menu.keys[pygame.K_DOWN] = self.buttonDown
        Menu.keys[pygame.K_UP] = self.buttonUp
        Menu.keys[pygame.K_LEFT] = self.buttonLeft
        Menu.keys[pygame.K_RIGHT] = self.buttonRight
        Menu.keys[pygame.K_RETURN] = self.buttonSpace
        Menu.keys[pygame.K_p] = self.buttonP
#         Menu.keys[pygame.K_x] = self.fireTwo
        Menu.keys[pygame.K_b] = self.boom
        Menu.keys[pygame.K_ESCAPE] = self.quit

    def createEframes(self):  
        sprite_sheet = pygame.image.load("./SkybusterExplosion.jpg").convert()
        w = 170
        h = 170
        hpad = 75
        vpad = 35
        for i in range(5):
            for j in range(4):
                image = self.getImage(sprite_sheet,hpad +  j*(w + 2 * hpad), vpad+ i*(h + 2*vpad), w, h)
                Menu.eFrames.append(image)

    def getImage(self, source, x, y, w, h):
            image = pygame.Surface([w, h]).convert()
            image.blit(source, (0, 0), (x, y, w, h))
            image.set_colorkey((0,0,0))
            return image
 
 

if __name__ == '__main__':
    Menu()