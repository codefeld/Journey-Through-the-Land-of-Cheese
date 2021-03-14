import time
import sys
import os
import random
import game

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/100)

def levelpicker():
	clear()
	typing("Ah, I see. You want to play this game, eh?\n")
	typing("Well, you will want to pick a chapter to start on.\n")
	if "level 1" not in game.levelbeat:
		print("Here are your options:\nChapter 1) The Beginning")
		typing("Please type the chapter number of your choice.\n")
		levelchosen = ""
		while levelchosen not in ["1"]:
			levelchosen = input("> ")
		game.clear()
		if levelchosen == "1":
			game.level1()
	else:
		print("Here are your options:\nChapter 1) The Beginning\nChapter 2) The Journey")
		typing("Please type the chapter number of your choice.\n")
		levelchosen = ""
		while levelchosen not in ["1", "2"]:
			levelchosen = input("> ")
		game.clear()
		if levelchosen == "1":
			game.level1()
		if levelchosen == "2":
			game.level2()