import levels
import sys
import time
import random

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/100)

def newlevel():
	typing("Please press enter to continue.\n")
	input("> ")
	levels.levelpicker()