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

DECK_DIR = './decks/default/'
DECK_LIST = [('Blue_Robot.png','Blue_Robot.png'), ('Garden_Witch_.png', 'Garden_Witch_.png'),
             ('Happy_Boy_.png', 'Happy_Boy_.png'), ('Math_Girl_.png','Math_Girl_.png'), ('Science_Girl.png','Science_Girl.png'),
             ('Butterfly.png', 'Butterfly.png'), ('Green_Spaceship.png', 'Green_Spaceship.png'),  
             ('Happy_Girl_.png', 'Happy_Girl_.png'), ('Red_Bird.png', 'Red_Bird.png'), ('Science_Guy.png', 'Science_Guy.png')]

BACK_SIDE = DECK_DIR + 'Waves_Pattern.png'

TOP_CARDS_SPACE = 0
ROWS = 4
COLS = 5
CARDS_SPACING = 0.02

class Card(Image):
    def __init__(self, back_side, front_side, pair_num, **args):
        # calculate the space of cards, and thier size
        card_x_space = 1.0 / COLS
        card_x_size = card_x_space - CARDS_SPACING
        
        game_y_space = 1.0 - TOP_CARDS_SPACE
        card_y_space = game_y_space / ROWS
        card_y_size = card_y_space - CARDS_SPACING
        
        self.back_side = back_side
        self.front_side = front_side
        self.pair_num = pair_num
        self.card_up = False
        
        Image.__init__(self, source=back_side, keep_ratio=False, 
                       size_hint = [card_x_size, card_y_size], **args)
    
    def set_card_up(self):
        print self.front_side
        self.card_up = True
        self.source = self.front_side
    
    def set_card_down(self):
         self.card_up = False
         self.source = self.back_side
    
    def flip_card(self):
        if self.card_up:
            self.set_card_down()
        else:
            self.set_card_up()
        
def DeckHandler(deck_list, back_side):
    cards = []
    for pair_num, pair in enumerate(deck_list):
        cards += [Card(back_side=back_side, front_side=DECK_DIR + pair[ n ], pair_num=pair_num) for n in range(2)]
    random.shuffle(cards)
    return cards

class GameBoard:
    def __init__(self, cards, rows, cols, card_spacing=0.2, top_card_space=0):
        self.cards = cards
        self.rows = rows
        self.cols = cols
        self.card_spacing = card_spacing
        self.top_card_space = top_card_space
        
        # preparing
        self.card_array = [list() for row in range(rows)]
    
    def get_cards_cavas_positions():
        """ prepare the sizes and positions of all cards"""
        
        self.card_x_space = 1.0 / self.cols
        self.card_x_size = card_x_space - self.card_spacing
        
        game_y_space = 1.0 - self.top_card_space
        self.card_y_space = game_y_space / self.rows
        self.card_y_size = card_y_space - self.card_spacing
        
class FirstScreen(Screen):
    def on_touch_up(self, touch_event):
        clickx, clicky = touch_event.spos
        
        # understand which col clicked
        for i, position in enumerate(self.x_positions):
            if clickx < position:
                cardx = i
                break
        
        # understand which row clicked
        for i, position in enumerate(self.y_positions):
            if clicky < position:
                cardy = i
                break
        
        self.card_list[cardy][cardx].flip_card()
        
class SecondScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class RtkApp(App):
    def build(self):
        deck = DeckHandler(deck_list=DECK_LIST, back_side=BACK_SIDE)
        root_widget = Builder.load_file('rtk.kv')
        pong_screen = root_widget.screens[0]

        # calculate the space of cards, and thier size
        card_x_space = 1.0 / COLS
        card_x_size = card_x_space - CARDS_SPACING
        
        game_y_space = 1.0 - TOP_CARDS_SPACE
        card_y_space = game_y_space / ROWS
        card_y_size = card_y_space - CARDS_SPACING
        
        pong_screen.card_list = [ list() for _ in range(ROWS) ]
        
        # calculate expected positions of the cards
        pong_screen.x_positions = [(card_x_space * (j+1)) - (CARDS_SPACING / 2) for j in range(COLS)]
        pong_screen.y_positions = [(card_y_space * (i+1)) for i in range(ROWS)]
        
        for i in range(ROWS):
            for j in range(COLS):
                new_card = deck.pop()
                new_card.pos_hint = {'top': pong_screen.y_positions[i], 'right': pong_screen.x_positions[j]}
                pong_screen.card_list[i].append(new_card)
                pong_screen.add_widget(pong_screen.card_list[i][j])
                
        return root_widget

if __name__ == '__main__':
    RtkApp().run()
