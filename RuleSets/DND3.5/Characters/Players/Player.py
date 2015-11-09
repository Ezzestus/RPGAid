#!/usr/bin/python
#Created by David Klumpenhower
#Created November 11, 2015
#DND Player Character module
import glob
import os

class Player(Character):
    characterType = 'player'
    ruleset = 'DnD3.5'
    
    def __init__(self, name, age, playerName, strength, constitution, dexterity, wisdom, inteligence, charisma):
        self.playerName = 
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.inteligence = inteligence
        self.charisma = charisma

   
def createCharacter(name, age, strength, constitution, dexterity, wisdom, inteligence, charisma):
    charName = Character(name, age, strength, constitution, dexterity, wisdom, inteligence, charisma) 
    return charName

def characterQuery():
    characterNames = []
    for characters in glob.glob('./Characters/*.char'):
        characterNames.append(os.path.basename(characters))
        return characterNames