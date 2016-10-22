#!/usr/bin/python
#Created by David Klumpenhower
#Created November 11, 2015
#DND Player Character module
import glob
import os

class Player(Character):
    characterType = 'player'
    ruleset = 'DnD3.5'

    def __init__(self, name, age, playerName, strength, constitution, dexterity, wisdom, intelligence, charisma):
        self.playerName = playerName
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @property
    def playerName(self):
        return self._playerName
    @playerName.setter
    def playerName(self, var):
        self._playerName = var

    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self, val):
        self._strength = val

    @property
    def constitution(self):
        return self._constitution
    @constitution.setter
    def constitution(self, val):
        self._constitution = val

    @property
    def dexterity(self):
        return self._dexterity
    @dexterity.setter
    def dexterity(self, val):
        self._dexterity = val

    @property
    def wisdom(self):
        return self._wisdom
    @wisdom.setter
    def wisdom(self, val):
        self._wisdom = val

    @property
    def intelligence(self):
        return self._intelligence
    @intelligence.setter
    def intelligence(self, val):
        self._intelligence = val

    @property
    def charisma(self):
        return self._charisma
    @charisma.setter
    def charisma(self, val):
        self._charisma = val

    def createCharacter(name, age, strength, constitution, dexterity, wisdom, inteligence, charisma):
        charName = Character(name, age, strength, constitution, dexterity, wisdom, inteligence, charisma)
        return charName

    def characterQuery():
        characterNames = []
        for characters in glob.glob('./Characters/*.char'):
            characterNames.append(os.path.basename(characters))
            return characterNames
