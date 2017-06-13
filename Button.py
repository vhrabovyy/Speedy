import pygame, time, random, sys, os
import Globals as gl
from Text import Text

class Button:
    func = {}
    
    def __init__(self, text=None, function=None,
                 background = pygame.color.THECOLORS['darkgreen'],
                 on_hover = pygame.color.THECOLORS['green'],
                 position=(0,0),
                 font_size = 30,
                 text_color = pygame.color.THECOLORS['black'],
                 width = 100,
                 height = 50,
                 font = 'fm3.ttf'):
        self.text = text
        self.function = function
        self.background = background
        self.background_image = False
        self.on_hover = on_hover
        self.position = position
        self.font_size = font_size
        self.text_color = text_color
        self.font = pygame.font.Font(os.path.join(os.getcwd(), 'fonts',font), font_size)

        self.parametry = []
        #przycisk z obrazkiem w tle(width, height - obrazka)
        if type(background) is str:
            self.background = pygame.image.load(os.path.join(os.getcwd(), 'img',background))
            self.background_rect = self.background.get_rect()
            self.background_rect.center = self.position
            self.background_image = True
        else:
            self.width = width
            self.height = height

        #
        if type(on_hover) is str:
            self.on_hover = pygame.image.load(on_hover)
            self.on_hover_rect = self.on_hover.get_rect()
            self.on_hover_rect.center = self.position


    def place(self, center=None, sleep=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if center:
        #position - centr button'a
            if self.background_image:
                if self.background_rect.x < mouse[0] < self.background_rect.x+self.background_rect.width and self.background_rect.y < mouse[1] < self.background_rect.y+self.background_rect.height:
                    gl.gameDisplay.blit(self.on_hover,self.on_hover_rect)
                    if self.function is not None:
                        if click[0]:
                            if self.function[1]:
                                for i in range(1,len(self.function)):
                                    self.parametry.append(self.function[i])
                                Button.func[self.function[0]](self.parametry)
                            else:
                                Button.func[self.function[0]]()
                                    
                                    
                    if self.text:
                        text = Text(self.text,
                                self.on_hover_rect.center,
                                self.font_size, self.text_color)
                        text.draw(gl.gameDisplay, 'center')
                else:
                    gl.gameDisplay.blit(self.background,self.background_rect)
                    if self.text:
                        text = Text(self.text,
                                self.background_rect.center,
                                self.font_size, self.text_color)
                        text.draw(gl.gameDisplay, 'center')
            #malowanie prostokątu
            else:
                if self.position[0]-self.width//2 < mouse[0] < self.position[0]-self.width//2+self.width and self.position[1]-self.height//2 < mouse[1] < self.position[1]-self.height//2+self.height:
                    cent = pygame.draw.rect(gl.gameDisplay, self.on_hover,
                                    (self.position[0]-self.width//2,self.position[1]-self.height//2,self.width, self.height))
                    
                    #wykonanie funkcji po wciśnięciu
                    if self.function is not None:
                        if click[0]:
                            if self.function[1]:
                                for i in range(1,len(self.function)):
                                    self.parametry.append(self.function[i])
                                Button.func[self.function[0]](self.parametry)
                            else:
                                Button.func[self.function[0]]()
                    if self.text:
                        text = Text(self.text,
                                cent.center,
                                self.font_size, self.text_color)
                        text.draw(gl.gameDisplay, 'center')
                else:
                    cent = pygame.draw.rect(gl.gameDisplay, self.background,
                                    (self.position[0]-self.width//2,self.position[1]-self.height//2,self.width, self.height))
                    if self.text:
                        text = Text(self.text,
                                cent.center,
                                self.font_size, self.text_color)
                        text.draw(gl.gameDisplay, 'center')
                    
            
                
        #position - star cordinates of button       
        else:
            if self.background_image:
                if self.background_rect.x < mouse[0] < self.background_rect.x+self.background_rect.width and self.background_rect.y < mouse[1] < self.background_rect.y+self.background_rect.height:
                    gl.gameDisplay.blit(self.on_hover,self.on_hover_rect)
                    if self.function is not None:
                        if click[0]:
                            if self.function[1]:
                                for i in range(1,len(self.function)):
                                    self.parametry.append(self.function[i])
                                Button.func[self.function[0]](self.parametry)
                            else:
                                Button.func[self.function[0]]()
                    if self.text:
                        text = Text(self.text,
                                self.on_hover_rect.center,
                                self.font_size, self.text_color)
                        text.draw(gl.gameDisplay, 'center')
                else:
                    gl.gameDisplay.blit(self.background,self.background_rect)
                    if self.text:
                        text = Text(self.text,
                                self.background_rect.center,
                                self.font_size, self.text_color)
                        text.draw(gl.gameDisplay, 'center')
            #malowanie prostokątu
            else:
                if self.position[0]-self.width//2 < mouse[0] < self.position[0]-self.width//2+self.width and self.position[1]-self.height//2 < mouse[1] < self.position[1]-self.height//2+self.height:
                    cent = pygame.draw.rect(gl.gameDisplay, self.on_hover,
                                    (self.position[0]-self.width//2,self.position[1]-self.height//2,self.width, self.height))

                    
                    #wykonanie funkcji po wciśnięciu
                    if self.function is not None:
                            if click[0]:
                                if self.function[1]:
                                    for i in range(1,len(self.function)):
                                        self.parametry.append(self.function[i])
                                    Button.func[self.function[0]](self.parametry)
                                else:
                                    Button.func[self.function[0]]()

                    if self.text:
                            text = Text(self.text,
                                    self.cent.center,
                                    self.font_size, self.text_color)
                            text.draw(gl.gameDisplay, 'center')
        
                    

    
    #continue function
    def resume():
        if gl.pause:
            gl.pause = False
        else:
            pass
    
    func['resume'] = resume
         
    #exit function
    def exit_game():
        if gl.game_exit is False:
            gl.pause = False
            gl.game_exit = True
        else:
            pass
    func['exit_game'] = exit_game

    #close function
    def close():
        pygame.quit()
        sys.exit()
    func['close'] = close

    def start_game():
        if gl.game_start is False:
            gl.game_start = True
    func['start_game'] = start_game

    def game_difficulty():
         gl.game_menu = False
         while not gl.game_menu:
            level = 1
            for event in pygame.event.get():
                #czerwony krzyrzyk spowoduje wymuszone zamknięcie gry
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            gl.gameDisplay.blit(gl.menu_background,[0,0])
            back = Button(None, ('game_menu',None),
                          os.path.join(os.getcwd(), 'img','left_arrow.png'),
                          os.path.join(os.getcwd(), 'img','left_arrow_green.png'),
                          (50,50)
                          )
            back.place()

            difficulties = Text('DIFFICULTIES', (gl.WIDTH//2, gl.HEIGHT*0.1),
                                80, pygame.color.THECOLORS['red'])
            difficulties.draw(gl.gameDisplay, 'center')

            actual = Button("Mode: "+gl.difficulty, None,
                            pygame.color.THECOLORS['cyan'],
                            pygame.color.THECOLORS['cyan'],
                            (gl.WIDTH//2, gl.HEIGHT*0.2),
                            50,
                            pygame.color.THECOLORS['black'],
                            gl.WIDTH*0.5,
                            gl.HEIGHT*0.09)
            actual.place('center')
                            
            easy = Button("EASY", ("difficulty_set", 'easy'),
                          pygame.color.THECOLORS['darkgreen'],
                          pygame.color.THECOLORS['green'],
                          (gl.WIDTH//2, gl.HEIGHT*0.3),
                          80,
                          pygame.color.THECOLORS['black'],
                          gl.WIDTH*0.4,
                          gl.HEIGHT*0.1)
            easy.place('center')

            medium = Button("MEDIUM", ("difficulty_set", 'medium'),
                          pygame.color.THECOLORS['yellow3'],
                          pygame.color.THECOLORS['yellow'],
                          (gl.WIDTH//2, gl.HEIGHT*0.5),
                          80,
                          pygame.color.THECOLORS['black'],
                          gl.WIDTH*0.4,
                          gl.HEIGHT*0.1)
            medium.place('center')
        
            hard = Button("HARD", ("difficulty_set", 'hard'),
                          pygame.color.THECOLORS['orangered2'],
                          pygame.color.THECOLORS['orangered'],
                          (gl.WIDTH//2, gl.HEIGHT*0.7),
                          80,
                          pygame.color.THECOLORS['black'],
                          gl.WIDTH*0.4,
                          gl.HEIGHT*0.1)
            hard.place('center')

            god = Button("GOD", ("difficulty_set", 'GOD'),
                          pygame.color.THECOLORS['darkred'],
                          pygame.color.THECOLORS['red'],
                          (gl.WIDTH//2, gl.HEIGHT*0.9),
                          80,
                          pygame.color.THECOLORS['black'],
                          gl.WIDTH*0.4,
                          gl.HEIGHT*0.1)
            god.place('center')
            pygame.display.update()
            #ustawianie zegaru na 60 odświeżeń na sekundę
            gl.clock.tick(20)
    
    func['game_difficulty'] = game_difficulty

    def game_menu():
        gl.game_menu = True
    func['game_menu'] = game_menu

    def difficulty_set(diff):
        gl.difficulty = diff[0]
        display = Button("Difficulty set", None,
                   pygame.color.THECOLORS['white'],
                   pygame.color.THECOLORS['white'],
                   (gl.WIDTH//2, gl.HEIGHT//2),100,
                   pygame.color.THECOLORS['black'],
                  gl.WIDTH,
                   100)
        display.place('center','sleep')
        
        

    
    func['difficulty_set']= difficulty_set

    def main_menu():
        gl.game_start = False
        gl.game_exit=True
        gl.game_menu = True
        gl.pause = False
    func['main_menu'] = main_menu
            
            
