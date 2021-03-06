import pygame as pg
import sys
from alien import Alien
from vector import Vector
from button import Button

# USE FOR BACKGROUND IMAGE
from sound import Sound
from settings import Settings

# from tkinter import *

# ws = Tk()
# ws.title('Space Invaders')
# ws.geometry('1500x1000')

# img = PhotoImage(file="game_images/outer_space/space_1.png")
# label = Label(
#     ws,
#     image=img
# )
# label.place(x=0, y=0)

# ws.mainloop()


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
YELLOW = (255, 255, 0)

class LandingPage:
    
    # LOADING IMAGES  
    ufo_imgs = [pg.transform.rotozoom(pg.image.load(
        f'game_images/alien_ship/alien_ship_{n}.png'), 0, 0.7) for n in range(2)]
    alien_one_imgs = [pg.transform.rotozoom(pg.image.load(f'game_images/aliens/alien_walk_2{n}.png'), 0, 0.25) for n in range(6)]
    alien_two_imgs = [pg.transform.rotozoom(pg.image.load(f'game_images/aliens/alien_walk_1{n}.png'), 0, 0.25) for n in range(6)]
    alien_tre_imgs = [pg.transform.rotozoom(pg.image.load(f'game_images/aliens/alien_walk_0{n}.png'), 0, 0.25) for n in range(6)]
   

    def __init__(self, game):
        self.sound = game.sound
        self.screen = game.screen
        self.landing_page_finished = False
        self.highscore = game.stats.get_highscore()

        headingFont = pg.font.SysFont(None, 192)
        # subtitleFont = pg.font.SysFont(None, 5)
        subheadingFont = pg.font.SysFont(None, 122)
        font = pg.font.SysFont(None, 48)

        strings = [
            ('SPACE', WHITE, headingFont), 
            # ('___   ', WHITE, subtitleFont),
            ('INVADERS', GREEN, subheadingFont),
            ('= 80 PTS', GREY, font),
            ('= 40 PTS', GREY, font), 
            ('= 20 PTS', GREY, font),
            ('= 10 PTS', GREY, font), 
            (f'HIGH SCORE = {self.highscore:,}', GREY, font),
            # ('PLAY GAME', GREEN, font), 
        ]

        self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in strings]

        self.posns = [150, 230]
        alien = [65 * x + 350 for x in range(4)]
   
        self.posns.extend(alien)
        self.posns.append(730)

        centerx = self.screen.get_rect().centerx

        self.play_button = Button(self.screen, "PLAY GAME", ul=(centerx - 150, 650))

        n = len(self.texts)
        self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, 
                                centery=self.posns[i]) for i in range(n)]
        self.ufo = Alien(game=game, sound=self.sound, alien_index=3, 
                                image_list=LandingPage.ufo_imgs, v=Vector(), ul=(centerx - 145, 340))
        self.alien_one = Alien(game=game, sound=self.sound, alien_index=0, 
                                image_list=LandingPage.alien_one_imgs, v=Vector(), ul=(centerx - 105, 385))
        self.alien_two = Alien(game=game, sound=self.sound, alien_index=1, 
                                image_list=LandingPage.alien_two_imgs, v=Vector(), ul=(centerx - 105, 450))
        self.alien_tre = Alien(game=game, sound=self.sound, alien_index=2, 
                                image_list=LandingPage.alien_tre_imgs, v=Vector(), ul=(centerx - 105, 515))

        self.hover = False

    def get_text(self, font, msg, color): return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect

    def mouse_on_button(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)
    
    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.KEYUP and e.key == pg.K_p:   # pretend PLAY BUTTON pressed
                self.landing_page_finished = True        
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_button():
                    self.landing_page_finished = True
            elif e.type == pg.MOUSEMOTION:
                if self.mouse_on_button() and not self.hover:
                    self.play_button.toggle_colors()
                    self.hover = True
                elif not self.mouse_on_button() and self.hover:
                    self.play_button.toggle_colors()
                    self.hover = False

    def update(self):       # TODO make aliens move
        pass 

    def show(self):
        while not self.landing_page_finished:
            self.update()
            self.draw()
            self.check_events()   # exits game if QUIT pressed

    def draw_text(self):
        n = len(self.texts)
        for i in range(n):
            self.screen.blit(self.texts[i], self.rects[i])

    def draw(self):
        self.screen.fill(BLACK)
        self.alien_one.draw()
        self.alien_two.draw()
        self.alien_tre.draw()
        self.ufo.draw()
        self.draw_text()
        self.play_button.draw()
        
        # self.alien_fleet.draw()   # TODO draw my aliens
        # self.lasers.draw()        # TODO dray my button and handle mouse events
        
        pg.display.flip()
        