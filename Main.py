import pygame, time, random, sys, os
import Globals as gl
from Text import Text
from Button import Button
from Game import Game
#Functionality that can by aded
#1. Different display resolutions - full screen mode
#2. Different levels
#4. Game menu
#5. 

pygame.init()


pygame.display.set_caption('{} v{}'.format(gl.CAPTION, gl.VERSION))

def game_menu():
        gl.game_menu = True
        while not gl.game_start:
            level = 1
            for event in pygame.event.get():
                #czerwony krzyrzyk spowoduje wymuszone zamknięcie gry
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            gl.gameDisplay.blit(gl.menu_background,[0,0])
            name = Text('SPEEDY', (gl.WIDTH//2, 0.15*gl.HEIGHT), 100,
                        pygame.color.THECOLORS['red'])
            name.draw(gl.gameDisplay,'center')
            
            start = Button('', ('start_game',None),
                          os.path.join(os.getcwd(), 'img','menu_item.png'),
                        os.path.join(os.getcwd(), 'img','menu_item_r1.png'),
                        (gl.WIDTH//2, 0.3*gl.HEIGHT),
                           50, pygame.color.THECOLORS['black'])
            
            start.place()
            start_text = Text('START!', (gl.WIDTH//2, 0.3*gl.HEIGHT+20),40)
            start_text.draw(gl.gameDisplay, 'center')
            
            levels = Button('', ('game_difficulty',None),
                            os.path.join(os.getcwd(), 'img','menu_item.png'),
                        os.path.join(os.getcwd(), 'img','menu_item_r1.png'),
                        (gl.WIDTH//2, 0.55*gl.HEIGHT),50,
                            pygame.color.THECOLORS['black'])

            levels.place()
            levels_text = Text('MODE', (gl.WIDTH//2, 0.55*gl.HEIGHT+20),40)
            levels_text.draw(gl.gameDisplay, 'center')

            exit_game = Button('', ('close',None),
                            os.path.join(os.getcwd(), 'img','menu_item.png'),
                        os.path.join(os.getcwd(), 'img','menu_item_r2.png'),
                        (gl.WIDTH//2, 0.80*gl.HEIGHT),50,
                               pygame.color.THECOLORS['black'])
            exit_game.place()
            exit_text = Text('EXIT', (gl.WIDTH//2, 0.80*gl.HEIGHT+20),40)
            exit_text.draw(gl.gameDisplay, 'center')
            

            
            #sprawdzanie zmiany poziomu
            if gl.difficulty == 'easy':
                    gl.car_speed = gl.difficulties['easy'][0]
                    gl.car_count = gl.difficulties['easy'][1]
            if gl.difficulty == 'medium':
                    gl.car_speed = gl.difficulties['medium'][0]
                    gl.car_count = gl.difficulties['medium'][1]

            if gl.difficulty == 'hard':
                    gl.car_speed = gl.difficulties['hard'][0]
                    gl.car_count = gl.difficulties['hard'][1]

            if gl.difficulty == 'GOD':
                    gl.car_speed = gl.difficulties['GOD'][0]
                    gl.car_count = gl.difficulties['GOD'][1]


            #sprawdzanie czy nie został wciśnięty start
            if gl.game_start:
                    gl.game_exit = False
                    game = Game()
                    game.game_loop()
                    time.sleep(2)
            pygame.display.update()
            #ustawianie zegaru na 60 odświeżeń na sekundę
            gl.clock.tick(20)



game_menu()

if gl.game_menu:
        game_menu()
pygame.quit()
sys.exit()





