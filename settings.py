from vector import Vector
from tkinter import *

class Settings:
    
    def __init__(self):
        
        # img = PhotoImage(file="game_images/outer_space/space_1.png")
        # label = Label(
        #     ws,
        #     image=img
        # )
        
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = img
        self.bg_color = 60, 60, 60

        self.ship_speed_factor = 3
        self.ship_limit = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = Vector(1, 0)
        
        # img = PhotoImage(file="game_images/outer_space/space_1.png")
        # label = Label(
        #     ws,
        #     image=img
        # )
        # label.place(x=0, y=0)

        self.laser_speed_factor = 3
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = 255, 0, 0
        
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
