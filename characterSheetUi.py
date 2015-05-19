#!/usr/bin/python
#Created by David Klumpenhower
#Created May 14, 2015
#

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Character:
	def __init__(self, strength):
		self.strength = 10
		
character1 = Character(10)

class CharacterUI(Widget):
    strength = NumericProperty(character1.strength)


class CharacterUIApp(App):
    def build(self):
        return CharacterUI()
    


if __name__ == '__main__':
    CharacterUIApp().run()
