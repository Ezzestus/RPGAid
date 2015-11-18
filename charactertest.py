#!/usr/bin/python
#Created by David Klumpenhower
#Updated by Romain Ruhlmann
#Created May 14, 2015
#Last update November 1, 2015
#Character module
import Character
import diceRoll
import numpy as np

stats_name = { "STR" : "Strength", "DEX" : "Dexterity", "CON" : "Constitution", "INT" : "Intelligence", "WIS" : "Wisdom", "CHA" : "Charisma"}

def print_stats(stats_value_dictionnary):
    #Prints the stats in a nice block form
    print("\nThese are your current stats")
    print("Strength     : " + str(int(stats_value_dictionnary["STR"])))
    print("Dexterity    : " + str(int(stats_value_dictionnary["DEX"])))
    print("Constitution : " + str(int(stats_value_dictionnary["CON"])))
    print("Intelligence : " + str(int(stats_value_dictionnary["INT"])))
    print("Wisdom       : " + str(int(stats_value_dictionnary["WIS"])))
    print("Charisma     : " + str(int(stats_value_dictionnary["CHA"])))

def generation_by_dice_rolling(hardness):
    #This is to generate the statistics using a dice rolling method
    """
    :param hardness will determine how the dice are rolled
    normal  : keep the 3 best dice roll out of 4 dice, using 6 rolls
    hard    : keep the 3 best dice roll out of 4 dice, using 7 rolls, the weakest one is thrown away
    godlike : keep the 3 best dice roll out of 5 dice, using 7 rolls, the weakest one is thrown away
    :return: an array of stats, in the order specified by user
    """
    # Set up the parameters
    best = 3
    if hardness == "normal" :
        out_of = 4
        rolls = 6
    elif hardness == "hard":
        out_of = 4
        rolls = 7
    elif hardness == "godlike":
        out_of = 5
        rolls = 7
    else :
        print("We assumed difficulty level is normal")
        out_of = 4
        rolls = 6

    statistics = np.zeros(7)
    # Roll the dice, grab the sequence (the [1]) instead of the result (See diceRoll for more info), discard the lowest results and add them
    for i in range(0, rolls):
        statistics[i] = np.sum(diceRoll.d(out_of, 6, 0)[1][out_of - best:])
    statistics = np.sort(statistics)[-6:][::-1] # Discard the lowest rice roll sort them ascendingly and reverse the order
    # Prepare the dictionnary
    stats_value_dico = {"STR" : statistics[0], "DEX" : statistics[1], "CON" : statistics[2], 
        "INT" : statistics[3], "WIS" : statistics[4], "CHA" : statistics[5]}
    print_stats(stats_value_dico)

    satisfied = input("Are you satisfied with this order? y/n ")
    while (satisfied != "y"):
        #Swap two stats at a time, until user chooses y
        print("Choose two statistics to exchange, in STR, DEX, CON, INT, SAG or CHA")
        first = input("First statistic\n")
        second = input("Second statistic\n")
        tmp = stats_value_dico[first]
        stats_value_dico[first] = stats_value_dico[second]
        stats_value_dico[second] = tmp
        print_stats(stats_value_dico)
        satisfied = input("Are you now satisfied with this order? y/n ")
    return stats_value_dico

def stat_to_points(n):
    """
    :param n: The numerical value of a stats, before adjustment
    :return: Its buy cost, according to : http://home.earthlink.net/~duanevp/dnd/stat_generation.htm
                at " Standard Point Buy "
    """
    if n < 14:
        return n - 8
    elif n < 17:
        return (n - 14) * 2 + 6
    else:
        return (n - 17) * 3 + 13

def stats_to_points(stats_value_dictionnary):
    """
    :param stats_value_dictionnary: A dictionnary of stats for which you want to know the total buy cost
    :return: The total cost of the last num results in the array array
    """
    cost = 0
    for name, value in stats_value_dictionnary.items():
        cost += stat_to_points(int(value))
    return cost

def are_stats_legal(stats_value_dictionnary):
    for name, value in stats_value_dictionnary.items():
        #if one of them doesn't fall in the allowed range, return false
        if (int(value) < 8) | (int(value) > 18):
            return False 
    #Otherwise, return true
    return True

def generation_by_points_buying(hardness):
    points = 28 # For normal
    if hardness == "hard":
        points = 32
    if hardness == "godlike":
        points = 35

    #prints the cost of all values
    print("Buy cost is as follow")
    for i in range(8, 19):
        print(str(i) + " costs " + str(stat_to_points(i)) + " points")

    done = False   
    while not(done):
        #Outer loop checks that the right number of points have been allowed and all stats fall in the normal range
        satisfied = "foo"
        while not(satisfied == "y"):
            # Middle loop asks if the user is satisfied with this assignment
            # If not, starts over
            stats_value_dico = {"STR" : 8, "DEX" : 8, "CON" : 8, "INT" : 8, "WIS" : 8, "CHA" : 8}
            points_spent = stats_to_points(stats_value_dico)
            while points_spent < points:
                #Inner loop goes on until all points have been assigned
                print("You have spent " + str(points_spent) + " points out of " + str(points) + ".\n"
                    +"You have " + str(points - points_spent) + " points remaining")
                stats_to_modify = input("Choose a stat to modify, in STR, DEX, CON, INT, SAG or CHA ")
                new_value = input("And choose its new value ")
                if stats_to_modify in stats_value_dico:
                    #Prevents the insertion of new keys in the dictionnary
                    stats_value_dico[stats_to_modify] = new_value
                else:
                    print("This statistic is not in the allowed statistics")
                print_stats(stats_value_dico)
                points_spent = stats_to_points(stats_value_dico)
            satisfied = input("Are you now satisfied with these stats? y/n ")
        if( (points_spent <= points) & are_stats_legal(stats_value_dico)):
            done =True
        else :
            print("There was an error in this assignment")
            print("Please check that all stast value fall in the allowed range and you haven't spent too many points")
            print("Starting over")
            print("...")
    return stats_value_dico

name = input("Enter a name for your Character: ");
age = input("Enter the age of your Character: ");
#What is this??? Asking for health?
"""
HEALF = input("What is your Health?")
print("You have ",HEALF," Health.")
"""

generation_type = "0"
while ((generation_type != "1") & (generation_type != "2")):
    generation_type = input("Do you want to get your stats via dice rolling or points? "+
        "\nChoose \n1 for dice rolling \n2 for the buy point system\n")

hardness = "foo"
while ((hardness != "normal") & (hardness != "hard") & (hardness != "godlike")):
    hardness = input("Choose the difficulty level of your campaign : normal, hard, godlike\n")
    # Note: the harder the campaign, the more powerful the character will be

if generation_type == "1":
    stats = generation_by_dice_rolling(hardness)
else:
    stats = generation_by_points_buying(hardness)

print(stats)
#stats is a dictionnary with keys being the 3 letters shorthand version of the characterisits, and the item, its value


charName = Character.createCharacter(name, age, stats["STR"], stats["DEX"], stats["CON"], stats["INT"], stats["WIS"], stats["CHA"])


exit = "false"
while (exit == "false"):
    printStat = input("What stat would you like to print for ")
    
    if (printStat == "exit"):
        exit = "true"
    elif printStat in stats:
        print (stats_name[printStat] + " : " + str(int(stats[printStat])))
    else:
        print_stats(stats)
