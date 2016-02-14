'''
Created on Feb 13, 2016

@author: saul
'''


        
import pygame
from componets.item import *
from math import cos,sin, pi
import random

class Bot(Item):
    
    def __init__(self, game, x, y, mode):
        super().__init__(x, y)
#         self.image = pygame.image.load("./res/a1.png").convert_alpha()
#         self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.modes = 3      #max number of modes. to cycle through
        self.mode = mode        # search mode int
        self.speed = 2      # rover current speed
        self.maxSpeed = 20  #max speed for time lapse
        self.angle = 0 
        self.amp = 10
        self.tick = 0
        self.maxtic = 100
        self.game = game
        self.vl = 0         #linear velocity
        self.va = 0         #angular velocity
        
        
    # ********************************************************
    # ***************** Modes go here! ********************
    # ********************************************************
    def update(self):
        vx = 0
        vy = 0
        if self.mode == 0:  #circle
            vx = self.amp * cos(self.speed*self.tick/pi)
            vy = self.amp * sin(self.speed*self.tick/pi)
        elif self.mode == 1:        #should be sprial
            vx = self.speed * sin(self.tick/pi)
            vy = self.speed 
        elif self.mode == 2:    
            vx = self.speed * self.amp * cos(self.rect.x/pi)
            vy = self.speed * self.amp * sin(self.rect.x/pi)
            
        elif self.mode == 3:    #wave 
            self.setV(self.speed, 0)
            vx = self.vl + sin(self.va)
            vy = self.vl + cos(self.va)
#             cart = self.convertToCart()
#             vx = cart[0]
#             vy = cart[1] 
            
            
        #check bounds
        if self.rect.y < 0 and vy < 0:
            vy = self.speed
        if self.rect.y > self.game.height and vy > 0:
            vy = -self.speed
        if self.rect.x > self.game.width and vx > 0:
            vx = -self.speed
        
        
        #update pos based on vx vy
        self.tick += 1
        if self.tick > self.maxtic:
            self.tick  = 0
                
        self.rect.x += vx
        self.rect.y += vy
          
        super().update()
        
    
    #set velocity, linear, anular
    #if we want to make it more like current ros control ros
    def setV(self, l, a):
        self.vl = l
        self.va = a
    
    #to do.. math..
    def convertToCartesian(self):
        x = 1
        y = 1
        result = [ x, y]
        return result
    
    def faster(self): 
        self.speed += 1
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
            
    def slower(self): 
        self.speed -= 1
        if self.speed < 0:
            self.speed = 0
            
    def nextMode(self):
        self.mode += 1
        if self.mode > self.modes:
            self.mode = 0
        
    def prevMode(self):
        self.mode -= 1
        if self.mode < 0:
            self.mode = self.modes
        