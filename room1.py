# (very very) Basic CYOA, start!

import time

def ladder_room():
	print("\nYou enter the room and find a rickety wooden ladder going upwards. Where the ladder seemingly exits, something like fresh air flows down. Reaching forward, you grasp the first rung and begin climbing...", flush=True)
	time.sleep(3)
	print("\nYou emerge into the fresh air. Congratulations!", flush=True)
	time.sleep(2)
	exit
	
print("\nYour eyes slide open. You find yourself laying on a cool stone floor, fully clothed in tunic and trousers, yet nothing else.")
print("\nRising to your feet, you look around. Directly ahead of you, a wooden door marked \"North\" is visible. You notice other doors: one to your left and one to your right, facing the first door, and one directly opposite the first door.") 

door = input("\nWhich do you decide to open? (Type \"north\", \"east\",\"south\", or \"west\" without quotes) \n")

if door == "east": 
	ladder_room()

