#!/usr/bin/python
#Created by David Klumpenhower
#Created May 14, 2015
#Load Character module

import glob
import os

def characterQuery():
	characterNames = []	
	
	for characters in glob.glob('./Characters/*.char'):
	
		characterNames.append(os.path.basename(characters))



	return characterNames