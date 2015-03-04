class Player():
	def __init__(self, p_class, health, mana, strength):
		self.p_class = p_class
		self.health = health
		self.mana = mana
		self.strength = strength


print "What hero do you want to be?"
print "1 for prince, 2 for knight, 3 for archer"
print "prince is healthier, knight is stronger,"
print "archer is mana-ier...whatever that means"
choice = int(input('player choice: '))
if choice == 1:
	player_1 = Player('Prince', 120, 10, 10)
	print " "
	print "Prince (not the symbol)"
	print "health starts at 120"
	print "mana starts at 10"
	print "strength starts at 10"
elif choice == 2:
	player_1 = Player('Knight', 80, 15, 16)
	print " "
	print "Knight in rusty armor"
	print "health starts at 80"
	print "mana starts at 15"
	print "strength starts at 16"
elif choice == 3:
	player_1 = Player('Archer', 100, 25, 12)
	print " "
	print "Archer (for lack of a better choice)"
	print "health starts at 100"
	print "mana starts at 25"
	print "strength starts at 12"

class Monster():
	def __init__(self, name, health, strength):
		self.name = name
		self.health = health
		self.strength = strength

rooms = {1 : {"name": "Troll's Bridge"}, 
		2 : {"name": "Goblin's Turkey Farm"}, 
		3 : {"name": "Colder Than A Witch's ....."},
		4 : {"name": "Hell, AKA the American South"},
		5 : {"name": "Trading Post"}}

def trading_post():
	print "entering the Trading Post..."
	print "you can buy health potions and upgrade strength"
	print "1 mana for 5 health potions"
	print "5 mana to upgrade strength points by 1"	
	choice = raw_input("what would you like to purchase, health or strength? \n \
1: health \n \
2: strength: ")
	if choice.lower() == "h" or choice.lower() == "health" or choice == "1":
		print "your health is currently:"
		print player_1.health
		print "your mana total is:"
		print player_1.mana
		print "the maximum you can purchase is:"
		print (player_1.mana*5)
		health = int(input("how much would you like to purchase? \n \
no change given, so multiples of 5 advised: "))
		if health <= (player_1.mana*5):
			player_1.health += health
			player_1.mana -= (health/5)
			main_menu()
		else: 
			print "you don't have enough currency for that..."
			main_menu()
	elif choice.lower() == "s" or choice.lower() == "strength" or choice == "2":
		print "your strength is currently:"
		print player_1.strength
		print "your mana total is:"
		print player_1.mana
		print "the maximum you can purchase is:"
		print (player_1.mana/5)
		strength = int(input("how much would you like to purchase? : "))
		if strength <= (player_1.mana/5):
			player_1.strength += strength
			player_1.mana -= (strength*5)
			main_menu()
		else: 
			print "you don't have enough currency for that..."
			main_menu()
	else:
		print "The trading post owner doesn't tolerate that malarky. \n \
Come back when you learn to type, he bellows. \n \
 "
		main_menu()

def Troll():
	troll = Monster("Troll", health = 40, strength = 8)
	while troll.health > 0 and player_1.health > 0: 
		choice = raw_input("what do you want to do?  \n \
1. attack \n \
2. retreat: ")
		if choice == "1" or choice.lower() == "attack":
			print "you attack!"
			player_1.health -= troll.strength
			troll.health -= player_1.strength
			print "your current health:"
			print player_1.health		
			print "Troll's health:"
			print troll.health
	
		elif choice == "2" or choice.lower() == "retreat":
				main_menu()
		else:
			print " "
			print "seriously?  read your options again there, brainiac...."
			print " "
	if player_1.health > 0:
		print "The troll jumps back under the bridge.  Nice work."
		print "You gained 6 mana for your troubles."
		player_1.mana += 6 
		main_menu()
	if troll.health > 0:
		print "you lose."
		print "GAME OVER"
		exit()

def Goblin():
	goblin = Monster("Goblin", health = 50, strength = 10)
	while goblin.health > 0 and player_1.health > 0: 
		choice = raw_input("what do you want to do?  \n \
1. attack \n \
2. retreat: ")
		if choice == "1" or choice.lower() == "attack":
			print "you attack!"
			player_1.health -= goblin.strength
			goblin.health -= player_1.strength
			print "your current health:"
			print player_1.health		
			print "Goblin's health:"
			print goblin.health
	
		elif choice == "2" or choice.lower() == "retreat":
				main_menu()
		else:
			print " "
			print "seriously?  read your options again there, brainiac...."
			print " "
	if player_1.health > 0:
		print "The goblin retreats.  Nice work."
		print "You gained 10 mana for your troubles."
		player_1.mana += 10 
		main_menu()
	if goblin.health > 0:
		print "no more health."
		print "GAME OVER"
		exit()

def Witch():
	witch = Monster("Witch", health = 70, strength = 15)
	while witch.health > 0 and player_1.health > 0: 
		choice = raw_input("what do you want to do?  \n \
1. attack \n \
2. retreat: ")
		if choice == "1" or choice.lower() == "attack":
			print "you attack!"
			player_1.health -= witch.strength
			witch.health -= player_1.strength
			print "your current health:"
			print player_1.health		
			print "Witch's health:"
			print witch.health
	
		elif choice == "2" or choice.lower() == "retreat":
				main_menu()
		else:
			print " "
			print "seriously?  read your options again there, brainiac...."
			print " "
	if player_1.health > 0:
		print "The witch flies away.  Nice work."
		print "You gained 15 mana for your troubles."
		player_1.mana += 15 
		main_menu()
	if witch.health > 0:
		print "you ran out of health."
		print "GAME OVER"
		exit()

def Diablo():
	diablo = Monster("Diablo", health = 100, strength = 20)
	while diablo.health > 0 and player_1.health > 0: 
		choice = raw_input("what do you want to do?  \n \
1. attack \n \
2. retreat: ")
		if choice == "1" or choice.lower() == "attack":
			print "you attack!"
			player_1.health -= diablo.strength
			diablo.health -= player_1.strength
			print "your current health:"
			print player_1.health		
			print "Diablo's health:"
			print diablo.health
	
		elif choice == "2" or choice.lower() == "retreat":
				main_menu()
		else:
			print " "
			print "seriously?  read your options again there, brainiac...."
			print " "
	if player_1.health > 0:
		print "El Diablo retiros.  Nice work."
		print "Not that you need it, but you gained 20 mana"
		player_1.mana += 20 
		main_menu()
	if diablo.health > 0:
		print "your health is depleted."
		print "GAME OVER"
		exit()

def main_menu():
	print "  "
	print "~CURRENT STATS~"
	print player_1.p_class
	print player_1.health
	print player_1.mana
	print player_1.strength
	print "  "
	print "Choose a room to enter:"
	print "1: "
	print rooms[1]["name"]
	print "2: " 
	print rooms[2]["name"]
	print "3: " 
	print rooms[3]["name"]
	print "4: " 
	print rooms[4]["name"]
	print "5: " 
	print rooms[5]["name"]
	print " "
	selection = raw_input("what room would you like to enter? (1-5): ")
	if selection == "1":
		print rooms[1]["name"]
		print " "
		print "The Troll awaits..."
		Troll()
	elif selection == "2":
		print rooms[2]["name"]
		print " "
		print "The Goblin awaits..."
		Goblin()
	elif selection == "3":
		print rooms[3]["name"]
		print " "
		print "The Witch awaits..."
		Witch()
	elif selection == "4":
		print rooms[4]["name"]
		print " "
		print "El Diablo awaits..."
		Diablo()
	elif selection == "5":
		print rooms[5]["name"]
		print " "
		trading_post()
	else: 
		print "1 through 5, buddy; this ain't rocket appliances"
		main_menu()

main_menu()
