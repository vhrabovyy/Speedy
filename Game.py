import pygame, time, random, sys, os
import Globals as gl
from Car import Car
from Text import Text
from Button import Button

class Game:
    best_score_easy = 0
    best_score_medium = 0
    best_score_hard = 0
    best_score_god = 0

    best_scores = {'easy': best_score_easy,
                   'medium': best_score_medium,
                   'hard': best_score_hard,
                   'GOD': best_score_god}
    
    def __init__(self, level=1, racecar=None, settings=None):
        #definiowanie objektu samochodu
        if racecar is None:
            self.racecar = Car(os.path.join(os.getcwd(), 'img','racecar.png'))
        else:
            self.racecar = Car(racecar)
        #grupa objektów samochodów
        self.car_group = pygame.sprite.Group()
        self.score = 0
        self.best_score = self.score
    
    def game_pause(self):

        pygame.mixer.music.pause()
        while gl.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gl.pause = not gl.pause      
            #gl.gameDisplay.blit(gl.background,[0,0])
            #wypisywanie Game Paused
            pause = Text("Game Paused", (gl.WIDTH//2, gl.HEIGHT//2), 100)
            pause.draw(gl.gameDisplay,'center')
            #Przyciski "Continue" i "Exit"
            resume = Button("Continue", ("resume",None),
                            pygame.color.THECOLORS['darkgreen'],
                            pygame.color.THECOLORS['green'], (gl.WIDTH*0.2, gl.HEIGHT//2+90),
                            25,
                            pygame.color.THECOLORS['black'],100,50)
            resume.place('center')
            
            main_menu = Button("Main menu", ("main_menu",None),
                               pygame.color.THECOLORS['yellow3'],
                               pygame.color.THECOLORS['yellow'], (gl.WIDTH*0.5, gl.HEIGHT//2+90),
                               25,
                               pygame.color.THECOLORS['black'],
                               150,50)
            main_menu.place('center')


            exit_game = Button("Exit", ("exit_game",None),
                               pygame.color.THECOLORS['darkred'],
                               pygame.color.THECOLORS['red'], (gl.WIDTH*0.8, gl.HEIGHT//2+90),
                               25,
                               pygame.color.THECOLORS['black'],
                               100,50)
            exit_game.place('center')
            
            pygame.display.update()
            gl.clock.tick(15)
        pygame.mixer.music.unpause()
            

    def check(self, event):
        if event.key == pygame.K_p:
            gl.pause = not gl.pause
            self.game_pause()
            
    def close(self):
        pygame.quit()
        sys.exit()
    
    def random_cordinates(self,car):
        # 3 position
        isx = 0
        isy = 0
        x = gl.position[random.randint(0,2)]
        while isx<2 and self.car_group:
            for c in self.car_group:
                if c.carrect.x != x[0]:
                    isx += 1
                else:
                    x = gl.position[random.randint(0,2)]
                    isx = 0
        y = random.randint(-1600,-self.racecar.carrect.height)
        while isy<2 and self.car_group:
            for c in self.car_group:
                if abs(abs(y)-abs(c.carrect.y)) > self.racecar.carrect.height:
                    isy += 1
                else:
                    y = random.randint(-1600,-self.racecar.carrect.height)
                    isy = 0
        car.place(x[0],y)
    def game_over(self):
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(gl.crash_sound)
                        
        colision = Text('Game Over', (gl.WIDTH//2,gl.HEIGHT//2), 100, pygame.color.THECOLORS['red'])
        colision.draw(gl.gameDisplay, 'center')
        gl.fuel = gl.fuel_reset
        gl.game_start = False
        gl.game_menu = True
        gl.game_exit = True


    def game_loop(self):

        #music
        pygame.mixer.music.play(-1)

        #ustaw samochod na początkową pozycję ekranu
        self.racecar.place(gl.center_position[0],gl.center_position[1])
    
        #randowanie pozycji samochodów
        for i in range(gl.car_count):
            car = Car(gl.cars[random.randint(0,5)])
            self.random_cordinates(car)
            self.car_group.add(car)

        fuel_reduce_event = pygame.USEREVENT + 1
        #zmniejszanie paliwa co fuel_reduce
        pygame.time.set_timer(fuel_reduce_event, gl.fuel_reduce)

        #resetowanie fuel
        gl.fuel = gl.fuel_reset
        while not gl.game_exit:
            for event in pygame.event.get():
                #czerwony krzyrzyk spowoduje wymuszone zamknięcie gry
                if event.type == pygame.QUIT:
                    self.close()
                #dla wszystkich innych przypadków przchwytuj i obsługuj aktywność użytkownika na powierzchni okna
                else:
                    #jeżeli wciśnięty klawisz na klawiaturze...
                    if event.type == pygame.KEYDOWN:
                        #sprawdź czy użytkownik nie zmienił położenia samochodu przez wciśnięcia klawisza
                        self.racecar.check(event)
                        #sprawdź czy użytkownik nie wcisnął klawisz funkcjonalny pauzy czy wyjścia do menu
                        self.check(event)
                    if event.type == pygame.KEYUP:
                        self.racecar.move(event)
                    if event.type == fuel_reduce_event:
                        if gl.fuel>=0:
                            gl.fuel -= 1
                        
            #wypełnienie powierzchni ekranu
            gl.gameDisplay.blit(gl.background,[0,gl.background_move])
            gl.gameDisplay.blit(gl.background,[0,-gl.backgroundrect.bottom+gl.background_move])

            #ustawianie samochodików
            for car in self.car_group:
                if car.carrect.y >= gl.HEIGHT or car.carrect.y >= self.racecar.carrect.y+40:
                    self.car_group.remove(car)
                    self.score +=1
                    car = Car(gl.cars[random.randint(0,5)])
                    self.random_cordinates(car)
                    self.car_group.add(car)
                #sprawdzanie kolizji
                if car.carrect.bottom >= self.racecar.carrect.y:
                    if car.carrect.x == self.racecar.carrect.x:
                        self.game_over()
                
                car.carrect.y+=gl.car_speed
                car.place()
            #sprawdzanie czy nie wyczerpało się paliwo
            if gl.fuel<=0:
                self.game_over()
                
            
            if(gl.background_move >= gl.HEIGHT):
                gl.background_move = 0
            else:
                gl.background_move += gl.speed

            #malowanie na dyspleju samochodu
            self.racecar.place()

            if(self.score > Game.best_scores[gl.difficulty]):
                            Game.best_scores[gl.difficulty] = self.score

            #wypisywanie rachunku
            score = Text("Score: "+str(self.score))
            score.draw(gl.gameDisplay)

            best_score = Text("Best score: "+
                              str(Game.best_scores[gl.difficulty]),
                              (0,gl.HEIGHT*0.05))
            best_score.draw(gl.gameDisplay)

            #paliwo wypisanie
            fuel = Car(gl.fuel_image,
                       gl.WIDTH-((pygame.image.load(gl.fuel_image)).get_rect().width+gl.WIDTH*0.02),
                       gl.HEIGHT*0.01)
            fuel.place()
            fuel_width = gl.WIDTH*0.02
            for i in range(gl.fuel):
                pygame.draw.rect(gl.gameDisplay, pygame.color.THECOLORS['red'],
                (gl.WIDTH-(gl.WIDTH*0.08+((i+1)*(fuel_width+5))),gl.HEIGHT*0.03, fuel_width,gl.HEIGHT*0.02))
                                 
            #odświeżanie ekranu
            pygame.display.flip()
            pygame.display.update()
            #ustawianie zegaru na 60 odświeżeń na sekundę
            gl.clock.tick(60)



    
