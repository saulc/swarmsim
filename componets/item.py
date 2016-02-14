'''
Created on Apr 28, 2015

@author: saul
'''
import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__();
        d = 50
        self.image = pygame.Surface([d, d])
        self.image.fill(pygame.Color(255,255,255))
        pygame.draw.circle(self.image, pygame.Color(200,100,200), [d//2,d//2], d//2, 0)
        self.image.set_colorkey( pygame.Color(255,255,255))

        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 0
        self.explode = False
        self.eFrame = 0
        self.eFrames = []
       
    def setEframe(self, frames): self.eFrames = frames   
        
    def getRect(self):
        return self.rect
       
    def getCenter(self):
        return (self.rect.x + self.image.get_width()//2, 
                self.rect.y + self.image.get_height()//2)
          
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def bang(self): self.explode = True
    
    def update(self):
        
        #print("eframe: " + str(self.eFrame) + " frames: " + str(len(self.eFrames)))
        if not self.explode:
            self.rect.x += self.vx
            self.rect.y += self.vy
        else:
            scale = 1   #control the speed of the explosion.
            self.eFrame += 1
            if self.eFrame >=  len(self.eFrames)-1: 
                self.eFrame = 0
                self.kill()
            else :
                self.image = self.eFrames[self.eFrame// scale]
          
          
        
       
          
          
          
            
        