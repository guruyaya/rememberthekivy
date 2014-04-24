''' Kivy super advanced memory game. No change in hell I'm finishing everything in time
'''
__version__ = '0.2'

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

TOP_CARDS_SPACE = 0.1
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
    def __init__(self, canvas, deck, rows, cols, cards_spacing=0.2, top_cards_space=0):
        self.canvas = canvas
        self.deck = deck
        self.rows = rows
        self.cols = cols
        self.cards_spacing = cards_spacing
        self.top_cards_space = top_cards_space
        
        # preparing
        self.card_array = [list() for row in range(rows)]
    
    def prepare_cards_cavas_positions(self):
        """ prepare the sizes and positions of all cards"""
        
        self.card_x_space = 1.0 / self.cols
        self.card_x_size = self.card_x_space - self.cards_spacing
        
        game_y_space = 1.0 - self.top_cards_space
        self.card_y_space = game_y_space / self.rows
        self.card_y_size = self.card_y_space - self.cards_spacing
        
        # calculate expected positions of the cards
        self.x_positions = [(self.card_x_space * (j+1)) - (self.cards_spacing / 2) for j in range(self.cols)]
        self.y_positions = [(self.card_y_space * (i+1)) for i in range(self.rows)]
    
    def position_cards_on_canvas(self):
        '''
        '''
        self.card_list = [ list() for _ in range(self.rows) ]
        for i in range(self.rows):
            for j in range(self.cols):
                new_card = self.deck.pop()
                new_card.pos_hint = {'top': self.y_positions[i], 'right': self.x_positions[j]}
                self.card_list[i].append(new_card)
                self.canvas.add_widget(new_card)
                
    def get_card_from_pos(self, clickx, clicky):
        '''
        '''
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
        
        return self.card_list[cardy][cardx]
    
class FirstScreen(Screen):
    def on_touch_up(self, touch_event):
        clickx, clicky = touch_event.spos
        self.game_board.get_card_from_pos(clickx, clicky).flip_card()
        
class SecondScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class RtkApp(App):
    def build(self):
        deck = DeckHandler(deck_list=DECK_LIST, back_side=BACK_SIDE)
        
        root_widget = Builder.load_file('rtk.kv')
        game_screen = root_widget.screens[0]
        game_screen.game_board = GameBoard(canvas=game_screen, deck=deck, rows=ROWS, cols=COLS, cards_spacing=CARDS_SPACING, top_cards_space=TOP_CARDS_SPACE)
        game_screen.game_board.prepare_cards_cavas_positions()
        game_screen.game_board.position_cards_on_canvas()               
        return root_widget

if __name__ == '__main__':
    RtkApp().run()
