import time
print("Star Civilian: A text-based RPG")
print("===============================")
time.sleep(1)


class scGame:
	
	# // Start Menu // #
	def runMenu():
		input("Press Enter to begin!")
		username = str(input("Enter a username: "))
		time.sleep(1)
		if username == "stanton":
			print("That username is taken!")
		elif username == "Stanton":
			print("That username is taken!")		
		else:
			print("Welcome to the 'verse", username, "!")
			f = open("username.txt", "w")
			f.write(username)
			f.close()
			time.sleep(1)
			print("--------------------------")
			time.sleep(1)
			print("Loading Game..")
			print("Pre-Loading Assets..")
			time.sleep(2)
			print("Loading complete!")
			print("Enjoy!")
			time.sleep(1)
			
	
	# // Setting a Home // #
	def setHome():
		print("--------------------------")
		time.sleep(1)
		print("Choose a Home location: ")
		Home_options = ["Port Olisar", "New Babbage", "Lorville", "Area18"]
		print(Home_options)
		Home = str(input("Select from above: "))
		if Home == "Port Olisar":
			print("You have selected Port Olisar")
			time.sleep(1)
			print("Enjoy your new Home!")
			print("--------------------------")
		elif Home == "New Babbage":
			print("You have selected New Babbage")
			time.sleep(1)
			print("Enjoy your new Home!")
			print("--------------------------")
		elif Home == "Lorville":
			print("You have selected Lorville")
			time.sleep(1)
			print("Enjoy your new Home!")
			print("--------------------------")
		elif Home == "Area18":
			print("You have selected Area18")
			time.sleep(1)
			print("Enjoy your new Home!")
			print("--------------------------")

	# // Choosing a starter ship // #
	def chooseShip():
		print("Choose a starter ship:")
		global starterShip
		starterShip = ["Aegis Stalker", "F7A Hornet", "CO. Mustang Alpha"]
		print(starterShip)
		starterShip = str(input("Which ship would you like? "))
		if starterShip == "Stalker":
			print("You have selected the Aegis Stalker")
			starterShip = "Aegis Stalker"
		elif starterShip == "Hornet":
			print("You have selected the Anvil F7A Hornet")
			starterShip = "Anvil F7A Hornet"
		elif starterShip == "Mustang Alpha":
			print("You have selected the CO. Mustang Alpha")
			starterShip = "CO. Mustang Alpha"
		else:
			print("Error: You have not selected a ship!")


	def profession():
		print("--------------------------")
		professions = "Bounty Hunter", "Mercenary", "Cargo Hauler", "Trader", "Smuggler"
		print("Available career paths: ",professions)
		career = str(input("Select the career you wish to take: "))
		time.sleep(1)
		print(" ")
		if career == "Bounty Hunter":
			print("You are now a Bounty Hunter!\n")
			time.sleep(1)
			if starterShip != "Aegis Stalker":
				print("Warning! You do not have the recommended ship to follow this career!")
				input("Press Enter to reset")
				#exit(starterShip != "Aegis Stalker")
			else:
				print("You have the", starterShip, ". Would you like to use this ship for all", career,"jobs?")
				input("Press Enter to continue")
		
		

	# // Module Runtime // #
	runMenu()
	time.sleep(1)
	setHome()
	time.sleep(1)
	chooseShip()
	time.sleep(1)
	profession()
	
	

#class shipStats(scGame):
	#def 

class userStats(scGame):
	def userStats(self, health, hunger, thirst, inventorySpace, stamina):
		self.health=health
		self.hunger=hunger
		self.thirst=thirst
		self.inventorySpace=inventorySpace
		self.stamina=stamina

	def get_userStats(self):
		return self.health
		return self.hunger
		return self.thirst
		return self.inventorySpace
		return self.stamina

	#defaultStats = {"userRank":0, "health":100, "hunger":10, "thirst":10, "inventorySpace":2000, "stamina":100}

	def defaultStats():
		userRank=0
		health=100
		hunger=10
		thirst=10
		inventorySpace=2000
		stamina=100

		
		

		



		


		
