''' Kivy super advanced memory game. No change in hell I'm finishing everything in time
'''
__version__ = '0.1'

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.image import Image

class PongGame(Widget):
    pass

class FirstScreen(Screen):
    def img_touch(self, touch_event):
        clickx, clicky = touch_event.spos
        cardx, cardy = (0,0)
        
        # understand which col clicked
        for i, position in enumerate(self.x_positions):
            if clicky < position:
                cardx = i
                break
        
        # understand which row clicked
        for i, position in enumerate(self.x_positions):
            if clickx < position:
                cardy = i
                break
            
        self.card_list[cardx][cardy].source = 'colours2.png'
        
class SecondScreen(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    pass

class Card(Image):
    def __init__(self, **args):
        Image.__init__(self, **args)
        
class RtkApp(App):
    def build(self):
        TOP_CARDS_SPACE = 0.3
        ROWS = 4
        COLS = 5
        CARDS_SPACING = 0.05
        # calculate the space of cards, and thier size
        card_x_space = 1.0 / COLS
        card_x_size = card_x_space - CARDS_SPACING
        
        game_y_space = 1.0 - TOP_CARDS_SPACE
        card_y_space = game_y_space / ROWS
        card_y_size = card_y_space - CARDS_SPACING
        
        root_widget = Builder.load_file('rtk.kv')
        pong_screen = root_widget.screens[0]
        pong_screen.on_touch_up = pong_screen.img_touch
        
        pong_screen.card_list = [ list() for _ in range(ROWS) ]
        
        # calculate expected positions of the cards
        pong_screen.x_positions = [(card_x_space * (j+1)) - (CARDS_SPACING / 2) for j in range(COLS)]
        pong_screen.y_positions = [(card_y_space * (i+1)) for i in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                pong_screen.card_list[i].append( 
                    Card(source='colours.png', size_hint=[card_x_size, card_y_size], allow_stretch=True, keep_ratio=False,
                          pos_hint={'top': pong_screen.y_positions[i], 'right': pong_screen.x_positions[j]}))
                pong_screen.add_widget(pong_screen.card_list[i][j])
                
        return root_widget

if __name__ == '__main__':
    RtkApp().run()
