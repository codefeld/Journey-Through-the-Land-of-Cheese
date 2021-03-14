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

def lose():
	if health <=0 or fullness <= 0:
		typing("Sadly, your levels have reached 0.\n")
		text.lost()
		newlevel()