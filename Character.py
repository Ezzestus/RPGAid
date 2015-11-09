#!/usr/bin/python
#Created by David Klumpenhower
#Created May 14, 2015
#Character module
import glob
import os

class Character:
    'Common base class for all Characters'
    def __init__ (self, name, age, gender, movementSpeed)
        self.name = name 
        self.age = age
        self.gender = gender
        self.movementSpeed = movementSpeed
    
