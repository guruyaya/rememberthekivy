
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class MainMenuScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class OptionsScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    pass
    
# beggining defigning the app
root_widget = Builder.load_file('rtk.pv')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()