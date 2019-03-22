import random
import time

#Definitions for character creation stuff. Also has some stuff for the rest of the game. Will finish later
def cold_eyes(text):
	print("\b")
def character_creation():
        print("")
def powers():
	print("")
def story_start():
	print("")
def main_game():
	print("")
def player_health():
	print("")
def enemy_health():
	print("")
def current_enemy_health():
	print("")
def current_player_health():
	print("")
def fighting():
	print("")
def volume_2():
	exec(open('Final_Superhero.py', encoding='utf8').read())
#SuperHero Games are cool
game = "start"
if game == "start":
	game_start = input("Welcome to Superhero game thing. In this game you create a superhero and save the world.\nDo you want to start? (Yes or no is fine).\n")
	if game_start == "yes":
		print ("Ok good. Here we go\n Also you can only fly ")
		character_creation = "running"
	#This is removed in the final game.
	elif game_start == "test":
		age = 16
		flight = True
		fighting = "Finished"
		current_player_health = 50
	elif game_start == "2":
		volume_2()
	else:
		print ("I gonna take that as a Yes!")
		character_creation = "running"

#Character Creation
while character_creation == "running":
	gender = input ("Do you want to be Male or Female?\n")
	if gender == "male":
		print ("Ok")
		male_character = "good"
		female_character = "bad"
		character_creation == "Stopped"
	if gender == "female":
		print ("Ok")
		female_character = "good"
		male_character = "bad"

	while male_character == "good":
		age = input ("How old is your character?\n")
		if age == 1:
			print("You are a bit young but its your choice!")
			character_creation = "Stopped"
			powers = "good"
			male_character = "bad"
		else:
			print("Ok. Lets Go")
			
			character_creation = "Stopped"
			powers = "good"
			male_character = "bad"
	while female_character == "good":
		if age == 1:
			print("You are a bit young but its your choice!")
			character_creation = "Stopped"
			powers = "good"
			female_character = "bad"
		else:
			print("Ok. Lets Go")
			character_creation = "Stopped"
			powers = "good"
			female_character = "bad"
	while powers == "good":
		superpowers = input ("out of these powers what ones do you want?\nFlight, Laser Eyes, Cold Breath, Super Strength, Invincibility, Super Speed, Super Intelligence\n")
		if superpowers == "flight":
			print ("Flight is a cool power.")
			powers = "bad"
			story_start = "good"
			flight = True
		if superpowers == "laser eyes":
			print ("lasers are cool.")
			powers = "bad"
			story_start = "good"
			laser = "good"
		if superpowers == "cold breath":
			print ("cold breath is a cool power.")
			powers = "bad"
			story_start = "good"
			cold = "good"
		if superpowers == "super strength":
			print ("super strength is a cool power.")
			powers = "bad"
			story_start = "good"
			strength = "good"
		if superpowers == "invincibility":
			print ("invincibility is a cool power.")
			powers = "bad"
			story_start = "good"
			cold = "good"

#Health, damage and enemies
player_health = 50
enemy_health = 60
enemies_list = ["Mutant"]
enemy_attacks_list = ["Punches", "Jumps on", "Kisses"]
enemy_attacks = random.choice(enemy_attacks_list)
enemy = random.choice(enemies_list)
enemy_damage_list = [3, 4]
enemy_damage = random.choice(enemy_damage_list)
player_attacks = ["fly", "punch"]
player_damage_list = [4, 6, 8]
player_damage = random.choice(player_damage_list)

#Attacks 
def attack_mode():
	print("You get taken down and fall unconcious")
	volume_2()
def fly_attack():
	print("You fly fowards and grab him. You then fly into the roof and slim him into it. You then drop him to the floor.\n")
	current_enemy_health = enemy_health - player_damage			
	print("The enemy", enemy_attacks, "you")
	current_player_health = player_health - enemy_damage
	print("Your health is", current_player_health)
	time.sleep(1.8)
def punch_attack():
	print("You run towards him and before they can attack you you punch him with all your strength.\nYou then kick him and throw him to the floor.\n")
	current_enemy_health = enemy_health - player_damage			
	print("The enemy", enemy_attacks, "you")
	current_player_health = player_health - enemy_damage
	print("Your health is", current_player_health)
	time.sleep(1.8)
def laser_weapon():
	current_enemy_health = current_enemy_health - 21
	print("You fire the weapon and a large laser bolt shoots out and hurts the enemy.")
	print("The enemy looks stunned.")
	attack_mode()
#Places the character can go to
#The start area
def battle1_end():
	print("You kill the", enemy, "however the fight has taken you into another room. There are 4 doors one leading into each direction.\n")
	main_game = True
def main_room():
	print("There are 4 doors one leading into each direction. What door do you enter?\n")

#Generic Stuff
def cant_decide():
	print("Lets try that again.")
	left_right1

#The west area
def west_wing():
	print("You go the west and enter the west wing of the complex and continue. ")
	print("You don't encounter anyone for a while but you do find a computer.")
	print("There is also a crossroads.")
	left_right1 = input("Do you go left or right?\n")
	if left_right1 == "left":
		diner()
	elif left_right1 == "right":
		kitchen()
	elif left_right1 == "hack":
		hack()
	else:
		cant_decide()
	if finished_attacking == True:
		print("You don't find anything of interest")
		main_room()
	else:
		print("")
def diner():
	diner = True
def kitchen():
	kitchen = True
def hack():
	print("You look at the computer and try to hack it.")
	time.sleep(60)
	play_game = input("You manage to hack the computer and on the desktop is an icon that says 'Superhero Game Thing.")
	if play_game == "play" or "play the game":
		print("You play the game and finish it. But you were so engrossed that you have become surrounded. You get taken away and put in jail. ")
		story_start = "end"
		fighting = False

#The east wing
def east_wing():
	print("You go the right and enter into what seems to be a housing area.")
	print("Each 'house' is just a room with a bed and a desk and a computer.")
	print("Each house is empty and the east wing is just a dead end. You go back to the main room.")
	main_room()

#The south wing
def south_wing():
	print("You can't get back up to the south wing.")
	main_room()

#The north are (This is where most of the game will go)
def north_wing():
	print("You go north and into a corridor. There are crossroads. One left and one right and one going straight.")
	left_right2 = input("What direction do you go in?\n").lower()
	if left_right2[0] == 'l':
		north_left()
	elif left_right2[0] == 'r':
		north_right()
	elif left_right2[0] == 'f':
		north_north()
def north_left():
	print("You go to the left and enter a room full of computers.")
	north_computers = input("")
	if north_computers == 'hack':
		print("You hack the computers and manage to get into the 'Restricted Files' section")
		print("It has a bunch of stuff about how they are testing mutants and crap.")
		print("You look behind you and see a perso with a nametag reading 'Dr Dimah'")
		print("She tazes you.")
		volume_2()
	else:
		print("Nothing else is really here.")
		main_room()
def north_right():
	print("You go to the right and find the armoury.")
	armoury_continue = input("There is a door that continues out the other end of the armoury. Do you go through it?\n")
	if armoury_continue[0] == 'y':
		print("You continue through the armoury.\n")
		time.sleep(.4)
		storage_room()
	else:
		armoury()
def armoury():
	print("Fun fact: You can pick stuff up if there is pick-upable stuff in the room. Just type take.\n")
	take_weapon = input("Do you take the weapons?\n")
	if take_weapon == 'take' or 'Take':
		print("The room has a defense mechanism. It kills you and everything goes black.")
		volume_2()
def storage_room():
	print("You go through the armoury and through the door.")
	print("You continue north and find someone.")
	doctor_dialogue()
def doctor_dialogue():
	print('The person is laying on the floor. They are clearly hurt and bleeding.')
	print('She has a badge on which reads "Dr Dimah".')
	talk_1 = input('"Can you help me?" She asks.\n')
	if talk_1[0] == 'y':
		print("You help her up and inspect her wounds. She thanks you for the assistance but recoils when she takes a look at your face.")
		print("You... you are mutant! She pulls out a gun and aims it at you. She calls for guards and you become surrounded.")
		attack_mode()
	else:
		print("She looks at you and sees that you are a mutant. She pulls out a gun and pulls the trigger.")
		volume_2()
#Start of the story
while story_start == "good":
	print("You the",age, "year old superhero. Have you come to save us? have you come to stop the evil threatening our world? I hope your answer is yes\n", time.sleep(1), "You wake up sweating. You just had a dream that something bad was going to happen and that you could stop it. But you can't. You are just a regular person. You don't have superpowers.")
	time.sleep(1.8)
	print("You check the time on your alarm clock. 3:51 AM. You look out of your window and see a bright light in the sky. The light gets bigger. And bigger. And bigger.Then it hits you. Literally. Everything goes dark\n")
	if flight == True:	
		print("You wake up. You look around you. Suddenly you shoot into the air. You hit your head on the roof and fall back down, but before you hit the ground you just hover.")
		time.sleep(1.0)
		print("You look around and the room is entirely white. White walls, white light. Even the bed you were on is white. A part of the wall lifts into the roof and opens into a white hallway.")
		time.sleep(1.6)
		print("A man in Black clothing with a black helmet and a gun sees you. He aims his gun.")
		time.sleep(.8)
		flight_1 = input("What do you do?\n(You can punch or fly.)\n")
		if flight_1 == "punch":
			print("You run towards him and before they can attack you you punch him with all your strength.\nYou then kick him and throw him to the floor.\n")
		elif flight_1 == "fly":
			print("You fly fowards and grab him. You then fly into the roof and slim him into it. You then drop him to the floor.\n")
		else:
			print("You fail miserably and get confused. You take ten damage.")
			current_player_health = player_health - 10
		current_enemy_health = enemy_health - player_damage			
		print("The enemy", enemy_attacks, "you")
		current_player_health = player_health - enemy_damage
		print("Your health is", current_player_health)
		time.sleep(.8)
		fighting = True
		while fighting == True:
			attacks = input("Do you punch him or use your fly attack?\n")
			if attacks == "punch":
				print("You run towards him and before they can attack you you punch him with all your strength.\nYou then kick him and throw him to the floor.\n")
			elif attacks == "fly":
				print("You fly fowards and grab him. You then fly into the roof and slim him into it. You then drop him to the floor.\n")
			elif attacks == "test":
				print("You better be actually testing this and not cheating. (This will probably be removed in the final version)")
				story_start = "end"
				fighting = "Finished"
			else:
				print("You get confused and fail. You take 10 damage from your failure. The enemy laughs")
				current_player_health = current_player_health - 10
			current_enemy_health = current_enemy_health - player_damage		
			print("The enemy", enemy_attacks, "you")
			current_player_health = current_player_health - enemy_damage
			print("Your health is", current_player_health)
			time.sleep(1.8)
			if current_player_health <=0:
				volume_2()
			elif current_enemy_health <=0:
				print("You kill the", enemy)
				story_start = "end"
				fighting = "Finished"
		time.sleep(.8)
#Main part of the game 
while fighting == "Finished":
	battle1_end()
	#This is the main game and its where it all starts. Once again a new while loop.
	while main_game == True:
		direction1 = input("What direction are you going in?\n").lower()
		if direction1[0] == "w":
			west_wing()
		elif direction1[0] == "s":
			south_wing()
		elif direction1[0] == "e":
			east_wing()
		elif direction1[0] == "n":
			north_wing()
		else:
			print("Lets try that again.")
			main_room()
		while diner == True:
			print("You go left and enter the diner. There is a bunch of", enemy, "in the room")
			print("They all look up and put their food down.")
			print("You realise that you have a fight on your hands")
			attack_mode()
		while kitchen == True:
			print("You go to the kitchen and find 3", enemy, ".")
			time.sleep(.7)
			print("You have a fight on your hands")
			attack_mode()

	
