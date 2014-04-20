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

def img_touch(touch_event):
   pass 
class PongGame(Widget):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    pass

class Card(Image):
    pass

class RtkApp(App):
    def build(self):
        TOP_CARDS_SPACE = 0.3
        ROWS = 4
        COLS = 5
        
        # calculate the space of cards, and thier size
        card_x_space = 1.0 / COLS
        card_x_size = card_x_space - 0.01
        
        game_y_space = 1.0 - TOP_CARDS_SPACE
        card_y_space = game_y_space / ROWS
        card_y_size = card_y_space - 0.01
        
        root_widget = Builder.load_file('rtk.kv')
        pong_screen = root_widget.screens[0]
        pong_screen.on_touch_up = img_touch
        
        card_list = [ list() for _ in range(ROWS) ]
        for i in range(ROWS):
            for j in range(COLS):
                card_list[i].append( 
                    Card(source='colours.png', size_hint=[card_x_size, card_y_size], allow_stretch=True, keep_ratio=False,
                          pos_hint={'top': (card_y_space * (i+1)), 'right': (card_x_space * (j+1)) - 0.005}))
                pong_screen.add_widget(card_list[i][j])
                
        return root_widget

if __name__ == '__main__':
    RtkApp().run()
