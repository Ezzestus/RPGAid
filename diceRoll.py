#!/usr/bin/python
#Created by David Klumpenhower
#Created May 11, 2015
#Dice Number Generation Python Script

import random

def diceRoller (die):
	die = die + 1
	roll = random.randrange (1, die)
	return roll
