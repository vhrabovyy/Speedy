import pygame, time, random, sys, os
import Globals as gl

class Bonus:
    list_bonus = []
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.bonusrect = self.image.get_rect()


        @property
        def bonusrect(self):
            return self._vonusrect
        @carrect.setter
        def bonusrect(self, new):
            self._bonusrect = new
            
        def place(self, x=None, y=None):
            if(x is not None):
                self.bonusrect.x = x
            if (y is not None):
                self.bonusrect.y = y
            
            #sprawdzanie pobrania
            if self.bonusrect.bottom >= gl.maincarrect.y:
                if self.bonusrect.x == gl.maincarrect.y:
                    del self
                    Game.flaga_refuel = False
                    Game.refuel_obj = False
                    if gl.fuel < gl.fuel_reset:
                        if gl.fuel+gl.fuel_reset//2>gl.fuel_reset:
                            gl.fuel = gl.fuel_reset
                        else:
                            gl.fuel += gl.fuel_reset//2
                del Game.refuel_obj
                Game.flaga_refuel = False
                Game.refuel_obj = False
                        
            elif Game.refuel_obj.carrect.y>=gl.HEIGHT:
                del Game.refuel_obj
                Game.flaga_refuel = False
                Game.refuel_obj = False
            else:
                Game.refuel_obj.carrect.y += 10

                
            gl.gameDisplay.blit(self.image,self.carrect)
        clockl = []
        sl = []
        def dodaj():
            clock = pygame.time.get_ticks()
            if len(Bonus.list_bonus) < 2:
                clockl.append(clock)
                sli = random.randint(1,10)*1000
            if clock in range((Game.cl_bonus+Game.i_bonus)-15,(Game.cl_bonus+Game.i_bonus)+15):
                x = gl.position[random.randint(0,2)]
                y = random.randint(1,200)
                Game.bonus_obj = Car(gl.bonusx2,x[0],-y)
            
            if Bonus.list_bonus:
                if len(Bonus.list_bonus) < 2:
                    Bonus.list_bonus.append(Bonus(gl.bonus))
            else:
                Bonus.list_bonus.append(Bonus(gl.bonus))
            
