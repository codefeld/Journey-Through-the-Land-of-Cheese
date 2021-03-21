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
	functions.newlevel()

def level2():
	global health
	global fullness
	typing("Welcome to the second level of this game.\n")
	typing("Your health and fullness levels have regenerated back to 20.\n")
	typing("However, when your levels subtract, I will not tell you your entire level; you will have to memorize it yourself.\n")
	typing("Now, lets get started.\n")
	time.sleep(1)
	clear()
	typing("You decide to explore the Land of Cheese.\n")
	typing("You leave your cheese hole and walk in a random direction.\n")
	time.sleep(1)
	typing("NO, NOT THAT WAY! THAT'S A CLIFF!\n")
	time.sleep(1)
	typing("Okay. You are back on track.\n")
	typing("You see a sign that says, \"You are now leaving the Swiss Cheese Valley, known for its bulls and nice cheese formations.\"\n")
	typing("Oh now you tell us about the bulls.\n")
	typing("Right behind the sign, you see another sign that says, \"Welcome to the Bleu Cheese Fields, known for its dangerous monsters and evil chickens\n")
	typing("You think to yourself, \"Evil Chickens? Uh-oh...\"\n")
	time.sleep(1)
	clear()
	typing("Walking through the Bleu Cheese Fields, you notice that the color of the terrain has gradually changed from a light yellow to a white color with blue specks.\n")
	fullness -= 5
	typing("You realize that you are starting to get hungry. Your fullness level went down 5.\n")
	typing("Then, you feel something pecking at the back of your ankle.\n")
	typing("You turn around to find a chicken the same color as the rest of the terrain you are in, except its eyes, which are red.\n")
	typing("For some reason, the chicken actually looks a little cute.\n")
	typing("You feel the sudden urge to pet it.\n")
	typing("As you reach down, the chicken makes a sound so loud it hurts your ears.\n")
	typing("Then hundreds of evil chickens suddenly appear.\n")
	time.sleep(1)
	clear()
	typing("All of the chickens run up to you and try to peck you.\n")
	typing("While doing so, you freak out.\n")
	typing("Here are some things you can do:\n")
	print("1) Fight\n2) Run")
	chickenescape = ""
	while chickenescape not in ["1", "2"]:
		chickenescape = input("> ")
	clear()
	if chickenescape == "1":
		typing("You defeated all of the chickens, since they are weak.\n")
		health -= 5
		typing("However, you lost 5 health doing so.\n")
	elif chickenescape == "2":
		typing("You try to run from the chickens.\n")
		typing("However, the chickens are faster than you thought.\n")
		text.lost()
		functions.newlevel()
	typing("Now that the chickens are no longer a problem, you decide to find some food.\n")
	typing("Do you like bleu cheese? (y/n)\n")
	bleucheese = ""
	while bleucheese not in ["y", "n"]:
		bleucheese = input("> ")
	clear()
	if bleucheese == "y":
		typing("It's a good thing that you like bleu cheese, since it's easy to find.\n")
		typing("You eat some of the bleu cheese ground, adding 5 to your fullness level.\n")
		fullness += 5
		typing("You decide to go and explore some more.\n")
		time.sleep(1)
		clear()
	elif bleucheese == "n":
		typing("That could be a problem.\n")
		typing("However, you have to eat.\n")
		typing("You decide that the best thing you can do is to journey out farther.\n")
		time.sleep(1)
		clear()
	fullness -= 5
	typing("After several hours of walking, you are still stuck in the Bleu Cheese Fields with no sign of a way out.\n")
	typing("Your fullness level also went down 5 again.\n")
	typing("You have no choice but to keep wandering.\n")
	time.sleep(1)
	clear()
	typing("Finally, you find something new. A sign that says \"Welcome to the Goat Cheese Mountains, known for its bad taste!\"\n")
	typing("\"Oh, come on!\" you say to yourself.\n")
	fullness -= 5
	typing("Your fullness level went down 5 again.\n")
	typing("Then, you see a goat made out of goat cheese charging at you.\n")
	typing("When it hits you, your health goes down 5.\n")
	health -= 5
	typing("The goat tries to charge at you again.\n")
	typing("This time, you barely manage to dodge it before it hits you.\n")
	typing("You need to come up with a decision before the goat charges you again.\n")
	typing("You find a chunk of goat cheese laying on the ground that you can use to shield yourself.\n")
	typing("The goat charges at you again, but because you have the shield, you only lose 2 health.\n")
	health -= 2
	typing("By then, the goat gives up and runs away.\n")
	typing("You are very hungry by now. The shield you have is edible, but you, like most people, hate goat cheese.\n")
	typing("You make the decision.\n")
	print("1) Eat the shield\n2) Don't eat the shield")
	yumyumshield = ""
	while yumyumshield not in ["1", "2"]:
		yumyumshield = input("> ")
	clear()
	if yumyumshield == "1":
		typing("The shield restores 10 fullness levels.\n")
		fullness += 10
		typing("It also restores 5 health levels.\n")
		typing("However, you dislike goat cheese, so, a few minutes later, you throw up, losing 5 health levels.\n")
	elif yumyumshield == "2":
		typing("You have decided to not eat the shield. You carry it along with you in case you find more goats.\n")
	time.sleep(1)
	clear()
	typing("As you walk through the Goat Cheese Mountains, you come across a large castle made of goat cheese.\n")
	typing("Would you like to explore the castle? (y/n)\n")
	cheesecastle = ""
	while cheesecastle not in ["y", "n"]:
		cheesecastle = input("> ")
	clear()
	if cheesecastle == "y":
		if yumyumshield == "2":
			typing("You hold up your shield, ready to protect yourself.\n")
		typing("You walk towards the castle.\n")
	elif cheesecastle == "n":
		typing("You decide not to explore the castle.\n")
		typing("You walk along the mountains until you see a sign that says, \"Welcome to the Parmesan Desert, known for its emptiness!\"\n")
		typing("As you start to walk into the desert, you find a goat made of goat cheese behind you.\n")
		typing("Goat - Hey, you! You aren't to be leaving here yet!\n")
		typing("He makes you follow him.\n")
		typing("A few minutes later, you find that he is leading you to the castle you saw earlier.\n")
	time.sleep(1)
	clear()
	typing("As you walk towards the castle, you find that it is surrounded by a moat made of milk.\n")
	fullness -= 5
	typing("You suddenly feel hungrier. Your fullness level went down 5.\n")
	functions.lose()
	typing("The goat brings you inside the castle, where you see a throne with a goat sitting on it.\n")
	typing("Unlike all of the other goats in the mountains, he is a real goat.\n")
	typing("Real Goat - I am Goaty McGoatcheese! You shall prepare for thy doom!\n")
	typing("Well, even though you are in trouble, you still beat the level.\n")
	text.win()
	typing("Also, there will be a third level coming very soon. Keep an eye out for it!\n")
	functions.newlevel()