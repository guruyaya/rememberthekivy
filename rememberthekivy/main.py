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
    print touch_event
    
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

class RtkApp(App):
    def build(self):
        root_widget = Builder.load_file('rtk.kv')
        pong_screen = root_widget.screens[0]
        pong_screen.on_touch_up = img_touch
        
        card_list = [ list() for _ in range(5) ]
        for i in range(5):
            for j in range(5):
                card_list[i].append( 
                    Image(source='colours.png', size_hint=[0.18,0.18], 
                          pos_hint={'top': (0.2 * (i+1)) - 0.01, 'right': (0.2 * (j+1)) - 0.01}))
                pong_screen.add_widget(card_list[i][j])
                
        return root_widget

if __name__ == '__main__':
    RtkApp().run()