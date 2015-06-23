#!/usr/bin/python
#Created by David Klumpenhower
#Created May 14, 2015
#Character module
import Character

name = input("Enter a name for your Character: ");
age = input("Enter the age of your Character: ");

strength = 10
constitution = 10
wisdom = 10
inteligence = 10
charisma = 10

charName = Character.createCharacter(name, age, 10, 10, 10, 10, 10)



exit = "false"

while (exit == "false"):
    printStat = input("What stat would you like to print for ")
    
    if (printStat == "exit"):
        exit = "true"
    elif (printStat == "str"):
        print ("str =", charName.strength)
    elif (printStat == "con"):
        print ("con =", charName.constitution)
    elif (printStat == "wis"):
        print ("wis =", charName.wisdom)
    elif (printStat == "int"):
        print ("int =", charName.inteligence)
    elif (printStat == "char"):
        print ("char =", charName.charisma)
    else:
        print ("str =", charName.strength)
        print ("con =", charName.constitution)
        print ("wis =", charName.wisdom)
        print ("int =", charName.inteligence)
        print ("char =", charName.charisma)