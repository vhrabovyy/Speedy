import pygame, time, random, sys, os

pygame.init()
#CONSTANTS #Nie zabiezpieczone przed zmianą ?
#Display
WIDTH = 733
HEIGHT = 800
DISPLAY = WIDTH, HEIGHT

#flagi dla set mode
FLAGS = pygame.FULLSCREEN, pygame.RESIZABLE
##pygame.FULLSCREEN    create a fullscreen display
##pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
##pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
##pygame.OPENGL        create an OpenGL-renderable display
##pygame.RESIZABLE     display window should be sizeable
##pygame.NOFRAME       display window will have no border or controls


#ZMIENNE
#Game_controll
pause = False
game_exit = False
game_start = False
game_menu = False
gameDisplay = pygame.display.set_mode(DISPLAY)
                                      #pygame.RESIZABLE |
                                      #pygame.HWSURFACE)
background = pygame.image.load(os.path.join(os.getcwd(), 'img','roads.png'))
backgroundrect = background.get_rect()
#menu background
menu_background = pygame.image.load(os.path.join(os.getcwd(), 'img','checkered-flag-background.png'))


carrect = pygame.image.load(os.path.join(os.getcwd(), 'img','racecar.png'))
carrect = carrect.get_rect()
car_move = 250
x_car_move = 0


right_position = ((WIDTH-carrect.width)//2+car_move, HEIGHT-carrect.height+40)
center_position = ((WIDTH-carrect.width)//2, HEIGHT-carrect.height)
left_position = ((WIDTH-carrect.width)//2-car_move, HEIGHT-carrect.height+40)
position = [right_position, center_position, left_position]
background_move = 0
speed = 3
car_count = 3
clock = pygame.time.Clock()

car_speed = 6

cars = [os.path.join(os.getcwd(), 'img','car2blue.png'),
        os.path.join(os.getcwd(), 'img','car2green.png'),
        os.path.join(os.getcwd(), 'img','car2red.png'),
        os.path.join(os.getcwd(), 'img','car2violet.png'),
        os.path.join(os.getcwd(), 'img','car2yellow.png'),
        os.path.join(os.getcwd(), 'img','car3blue.png')
        ]
#sounds
crash_sound = pygame.mixer.Sound(os.path.join(os.getcwd(), 'sounds','Crash.ogg'))
pygame.mixer.music.load(os.path.join(os.getcwd(), 'sounds','Proctor.ogg'))


#game difficulties
#first number car_speed, second - car count
difficulties = {'easy': (6,2),
                'medium': (8,2),
                'hard': (12,2),
                'GOD': (20,2)
                }
                
difficulty = 'easy'

difficult_set = False

#fuel control
fuel = 10

#Files

#os.path.join('img','racecarmy.png'))

#Version
VERSION = 0.0
#Caption(game name)
CAPTION = "Speedy"

#Functions
    
#Colors
#HTML representation of color.THECOLORS[]
##https://sites.google.com/site/meticulosslacker/pygame-thecolors
##pygame.color.THECOLORS['red']

#FUNCTIONS




