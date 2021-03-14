import time
import os
import sys
import random
from random import randint
import text
import functions

levelbeat = []
health = 20
fullness = 20

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*10/100)

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

def level1():
	global health
	global fullness
	typing("I see that you want to start Chapter 1.\n")
	typing("This will be the origin of how you got to the Land of Cheese.\n")
	time.sleep(1)
	typing("Unlike most text adventures you have played, some of the wrong paths don't cause you to lose the game; just health.\n")
	typing("If you lose all of your health, you have lost the game and start over.\n")
	typing("We will start by giving you a health number of 20 and a fullness number of 20 (this tracks your hunger).\n")
	typing("Okay, then. Let's begin!\n")
	time.sleep(1)
	clear()
	typing("Your story begins at your house in Wisconsin.\n")
	typing("Little did you know, but Wisconsin is the gateway to the Land of Cheese, which is where you'll end up.\n")
	typing("You walk down the street to go to the grocery store, so you can pick up some cheese.\n")
	typing("What kind of cheese do you want?\n")
	cheesetype = input("> ")
	chosencheese = cheesetype.lower()
	clear()
	if chosencheese == "goat" or "goat cheese":
		typing("BLEEEEEEEEEEEEEEEEGHHHH!\n")
	else:
		randomstatement = random.randint(1,3)
		if randomstatement == 1:
			typing("Oooooooooooooooooh! I like %s too!\n" % chosencheese)
		elif randomstatement == 2:
			typing("WHAT! YOU FOUND %s! I'VE BEEN LOOKING FOR THAT FOR FOREVER!\n" % chosencheese)
		elif randomstatement == 3:
			typing("Can you pick up some more %s for me?\n" % chosencheese)
	typing("You walk to the cheese aisle to grab all of the %s the store has.\n" % chosencheese)
	typing("However, you find something very peculiar: a button on the back of the shelf that says \"PUSH ME!\"\n")
	typing("What do you do?\n")
	print("1) Press the Button\n2) Ignore it.")
	button = ""
	while button not in ["1", "2"]:
		button = input("> ")
	clear()
	if button == "1":
		typing("You press the button.\n")
	elif button == "2":
		typing("You try to resist not pressing the button, but you can't help yourself.\n")
		typing("You push the button.\n")
	typing("That's when you suddenly find yourself in what is known as \"The Land of Cheese\".\n")
	time.sleep(1)
	clear()
	typing("You look around to find the terrain completely made of cheese.\n")
	typing("There is no sign of a way back or any towns and cities. You will have to explore.\n")
	typing("As for gathering food, that will be easy, since everything is edible, or is it?\n")
	fullness -= 5
	typing("Your fullness went down 5, so you are now at %s. If your fullness level reaches 0, you lose and will have to start the game over.\n" % fullness)
	typing("Then, you notice something moving. It happens to be a cow made completely of cheese.\n")
	typing("To get food, you can either try to eat the cheesy terrain, which may be poisonous, or try to hunt the cow, which could be dangerous.\n")
	print("Pick one:\n1) Eat the terrain\n2) Hunt the cow.")
	firstbite = ""
	while firstbite not in ["1", "2"]:
		firstbite = input("> ")
	clear()
	if firstbite == "1":
		typing("Before you eat it, you make sure the terrain is safe. Since the cow is eating it, I guess it's okay to eat.\n")
		typing("You eat the cheesy terrain.\n")
		typing("This cheese happens to be normal Swiss cheese.\n")
		fullness += 20
		typing("The terrain was safe to eat, and your fullness level is back at 20.\n")
	elif firstbite == "2":
		typing("You try to hunt the cow.\n")
		typing("Since the cow is one-hundred percent yellow, it is hard to tell that it was actually a bull.\n")
		typing("The bull attacks you.\n")
		health -= 5
		typing("You lose 5 health, bringing you down to %s.\n" % health)
		typing("You also didn't get anything to eat.\n")
	time.sleep(1)
	clear()
	typing("Looking up, you can see that it is starting to get dark.\n")
	if firstbite == "1":
		typing("You find a cheese hole that you can sleep in for the night.\n")
		typing("In the sky, there is a cheese sphere with a bite taken from it, giving it the shape of a cresent.\n")
		typing("You fall asleep, hoping you were just having a dream.\n")
		typing("You wake up in the morning.")
	elif firstbite == "2":
		fullness -= 5
		typing("However, your fullness level has dropped down 5 more from the bull battle.\n")
		typing("You are now at %s fullness, making you hungry.\n" % fullness)
		typing("You can decide what to do next:\n")
		print("1) Find food\n2) Find shelter")
		firstnight = ""
		while firstnight not in ["1", "2"]:
			firstnight = input("> ")
		clear()
		if firstnight == "1":
			typing("You go out to find some food.\n")
			typing("You find many cheese animals (cheesimals) sleeping in cheese holes along.\n")
			typing("However, taking a closer look, you find that they are all bulls.\n")
			typing("If you wake the bulls, they will try to attack you.\n")
			typing("However, you can take the risk you passed up earlier to try and eat the terrain.\n")
			typing("Which do you choose?\n")
			print("1) Hunt the bulls\n2) Eat the terrain")
			secondfirstbite = ""
			while secondfirstbite not in ["1", "2"]:
				secondfirstbite = input("> ")
			clear()
			if secondfirstbite == "1":
				randombull = random.randint(1, 2)
				if randombull == 1:
					typing("You were successfully able to hunt a bull.\n")
					fullness = 20
					typing("You eat with delight, and your fullness level is back at 20!\n")
				elif randombull == 2:
					typing("The bull you are trying to hunt wakes up and tries to attack you.\n")
					typing("This wakes up all of the other nearby bulls.\n")
					health -= 10
					typing("You made it away from them, but you lost 10 health. You are now at %s.\n" % health)
			elif secondfirstbite == "2":
				typing("You eat the cheesy terrain.\n")
				typing("This cheese happens to be normal Swiss cheese.\n")
				fullness = 20
				typing("The terrain was safe to eat, and your fullness level is back at 20.\n")
			typing("You decide to find some shelter.\n")
			typing("You find a cheese hole that you can sleep in for the night.\n")
			typing("In the sky, there is a cheese sphere with a bite taken from it, giving it the shape of a cresent.\n")
			typing("You fall asleep, hoping you were just having a dream.\n")
			health += 5
			typing("When you wake up, you find your health regenerated by 5 levels. You are now at %s.\n" % health)
		elif firstnight == "2":
			typing("You decide to find some shelter.\n")
			typing("You find a cheese hole that you can sleep in for the night.\n")
			typing("In the sky, there is a cheese sphere with a bite taken from it, giving it the shape of a cresent.\n")
			typing("You fall asleep, hoping you were just having a dream.\n")
			health += 5
			typing("When you wake up, you find your health regenerated by 5 levels. You are now at %s.\n" % health)
	typing("You are now ready to continue on with your journey!\n")
	text.win()
	if "level 1" not in levelbeat:
		levelbeat.append("level 1")
	if health <= 10 or fullness <= 10:
		typing("However, with your levels getting low, you will need to plan carefully for the next level.\n")
	functions.newlevel()

def level2():
	global health
	global fullness
	typing("Welcome to the second level of this game.\n")
	typing("You may remember the skill levels you ended the last level with.\n")
	typing("You health was %s and you fullness was %s.\n" % (health, fullness))
