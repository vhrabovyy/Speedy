import pygame, time, random, sys, os
import Globals as gl
class Car(pygame.sprite.Sprite):
    
    def __init__(self, image, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.carrect = self.image.get_rect()
        self.carrect.x = x
        self.carrect.y = y   

    @property
    def carrect(self):
        return self._carrect
    @carrect.setter
    def carrect(self, new):
        self._carrect = new
        
    def place(self, x=None, y=None):
        if(x is not None):
            self.carrect.x = x
        if (y is not None):
            self.carrect.y = y
        #print(self.carrect)
        gl.gameDisplay.blit(self.image,self.carrect)

    
    
    def check(self,event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
             self.go(event, "left")
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.go(event, "right")
            
        
    def go(self, event, direction):
        if direction == "left":
            if self.carrect.x > gl.left_position[0]:
                gl.x_car_move+=-gl.car_move 
            else:
                pass
        if direction == "right":
            if self.carrect.x < gl.right_position[0]:
                gl.x_car_move+=gl.car_move   
            else:
                pass
        self.carrect.x += gl.x_car_move
    def move(self, event):
        gl.x_car_move = 0

            
        
             
