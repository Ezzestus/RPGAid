#!/usr/bin/python
#Created by David Klumpenhower
#Created May 14, 2015
#

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty


class Character:
    def __init__(self, strength):
        self.strength = 10

character1 = Character(10)

class CharacterSheet(Widget):
    pass

class CharacterUIApp(App):
    def build(self):
        return CharacterSheet()

if __name__ == '__main__':
    CharacterUIApp().run()