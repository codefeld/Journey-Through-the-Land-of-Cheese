import time
import os
import levels
import sys
import game

game.clear()
print('''
     ___  _______  __   __  ______    __    _  _______  __   __    _______  __   __  ______    _______  __   __  _______  __   __ 
    |   ||       ||  | |  ||    _ |  |  |  | ||       ||  | |  |  |       ||  | |  ||    _ |  |       ||  | |  ||       ||  | |  |
    |   ||   _   ||  | |  ||   | ||  |   |_| ||    ___||  |_|  |  |_     _||  |_|  ||   | ||  |   _   ||  | |  ||    ___||  |_|  |
    |   ||  | |  ||  |_|  ||   |_||_ |       ||   |___ |       |    |   |  |       ||   |_||_ |  | |  ||  |_|  ||   | __ |       |
 ___|   ||  |_|  ||       ||    __  ||  _    ||    ___||_     _|    |   |  |       ||    __  ||  |_|  ||       ||   ||  ||       |
|       ||       ||       ||   |  | || | |   ||   |___   |   |      |   |  |   _   ||   |  | ||       ||       ||   |_| ||   _   |
|_______||_______||_______||___|  |_||_|  |__||_______|  |___|      |___|  |__| |__||___|  |_||_______||_______||_______||__| |__|
 _______  __   __  _______    ___      _______  __    _  ______     _______  _______    _______  __   __  _______  _______  _______  _______ 
|       ||  | |  ||       |  |   |    |   _   ||  |  | ||      |   |       ||       |  |       ||  | |  ||       ||       ||       ||       |
|_     _||  |_|  ||    ___|  |   |    |  |_|  ||   |_| ||  _    |  |   _   ||    ___|  |       ||  |_|  ||    ___||    ___||  _____||    ___|
  |   |  |       ||   |___   |   |    |       ||       || | |   |  |  | |  ||   |___   |       ||       ||   |___ |   |___ | |_____ |   |___ 
  |   |  |       ||    ___|  |   |___ |       ||  _    || |_|   |  |  |_|  ||    ___|  |      _||       ||    ___||    ___||_____  ||    ___|
  |   |  |   _   ||   |___   |       ||   _   || | |   ||       |  |       ||   |      |     |_ |   _   ||   |___ |   |___  _____| ||   |___ 
  |___|  |__| |__||_______|  |_______||__| |__||_|  |__||______|   |_______||___|      |_______||__| |__||_______||_______||_______||_______|
''')
print(".:PLAY:.")
print(".:EXIT:.")
print("")
x = ""
while x not in ["play", "PLAY", "exit", "EXIT"]:
	x = input("> ")
game.clear()
if x == "play" or "PLAY":
	levels.levelpicker()
elif x == "exit" or "EXIT":
	levels.typing("Why would you want to exit now? We are playing this game.\n")
	time.sleep(1)
	levels.levelpicker()