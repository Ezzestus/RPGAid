#!/usr/bin/python
#Created by David Klumpenhower
#Created May 14, 2015
#Character module
import glob
import os

class Character:
    'Common base class for all Characters'

    def __init__(self, name, age, strength, constitution, dexterity, wisdom, inteligence, charisma):
        self.name = name 
        self.age = age

        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.inteligence = inteligence
        self.charisma = charisma

   
def createCharacter(name, age, strength, constitution, dexterity, wisdom, inteligence, charisma):
    charName = Character(name, age, strength, constitution, dexterity, wisdom, inteligence, charisma) 
    return charName


def saveCharacter(character):
    derp=1



def characterQuery():
    characterNames = []
    for characters in glob.glob('./Characters/*.char'):
        characterNames.append(os.path.basename(characters))
        return characterNames