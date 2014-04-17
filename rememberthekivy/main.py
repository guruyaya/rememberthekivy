
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class MainMenuScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ColourScreen(Screen):
    colour = ListProperty([1., 0., 0., 1.])

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name

root_widget = Builder.load_file('rtk.pv')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()