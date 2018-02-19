# (very very) Basic CYOA, start!

import time

def quit_prompt():
	if input("Type q to quit: ") == "q":
		exit
	else:
		print("Please type 'q' and press Enter.")
		quit_prompt()

def ladder_room():
	print("\nYou enter the room and find a rickety wooden ladder going upwards. Where the ladder seemingly exits, something like fresh air flows down. Reaching forward, you grasp the first rung and begin climbing...", flush=True)
	time.sleep(3)
	print("\nYou emerge into the fresh air. Congratulations!", flush=True)
	time.sleep(2)
	quit_prompt()
	
def start_room():
	print("\nYour eyes slide open. You find yourself laying on a cool stone floor, fully clothed in tunic and trousers, yet nothing else.")
	print("\nRising to your feet, you look around. Directly ahead of you, a wooden door marked \"North\" is visible. You notice other doors: one to your left and one to your right, facing the first door, and one directly opposite the first door.") 
	start_room_menu()
	
def start_room_menu():
	door = input("\nWhich do you decide to open?\n")
	door = door.lower()

	if door == "north":
		time.sleep(1)
		print("\nThe door seems to be locked.")
		start_room_menu()
	elif door == "south":
		time.sleep(1)
		print("\nThe door seems to be locked.")
		start_room_menu()
	elif door == "west":
		time.sleep(1)
		print("\nThe door seems to be locked.")
		start_room_menu()
	elif door == "east":
		time.sleep(1)
		ladder_room()
	else:
		print("\nType an valid selection: north, east, south, west.\n")
		start_room_menu()
	
	
# Playtest
start_room()

