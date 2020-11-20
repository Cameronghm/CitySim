import pygame
import math
from Setup import *
from DrawBandO import *

#function to determine which tile the user has clicked on
def tileDeterminer(x, y, depressed, money, screen, population):
		#Sets the row and column that the user has clicked on
		column = x // (WIDTH + MARGIN)
		row = y // (WIDTH + MARGIN)
		#Road Conditions
		roadConditions = [[row,column-1],[row,column+1],[row-1,column],[row+1,column]]
		x = 4
		while x > -1:
			try:
				roadConditions[x-1] = Land[roadConditions[x-1][0]][roadConditions[x-1][1]]
			except:
				IndexError
			x -= 1
		#Sets values for each pressed button
		costs = [houseCost, apartmentCost, clearCost, powerCost, waterCost, roadCost, houseUpgradeCost, apartmentUpgradeCost]
		pygame.mixer.music.load('construction.mp3')
		#Will try to set the array position to the button pressed and will skip any Index errors
		try:
            #Will make it so if you haven't depressed a button you won't clear the tile
			for buttons in range(len(depressed)):
				if depressed[buttons] == 1:
					pressed = buttons + 1
			if pressed == 3:
				Land[row][column] = 0
			elif (money - costs[pressed-1]) >= 0:
				if (6 in roadConditions):
					if (pressed != 7 and pressed != 8) and Land[row][column] == 0:
						money = (money - costs[pressed-1])
						Land[row][column] = pressed
						pygame.mixer.music.play()
					if pressed == 7:
						if Land[row][column] == 7:
							money = (money - costs[pressed-1])
							Land[row][column] = 8
							pygame.mixer.music.play()
						if Land[row][column] == 1:
							money = (money - costs[pressed-1])
							Land[row][column] = 7
							pygame.mixer.music.play()
					if pressed == 8:
						if Land[row][column] == 9:
							money = (money - costs[pressed-1])
							Land[row][column] = 10
							pygame.mixer.music.play()
						if Land[row][column] == 2:
							money = (money - costs[pressed-1])
							Land[row][column] = 9
							pygame.mixer.music.play()
			elif (money - costs[pressed-1]) <= 0:
				if pressed == 1:
					createLabel(screen, WHITE, 25, 695, 145, 50, ("£" + str(houseCost)), RED, 15, False, False, True)
				if pressed == 2:
					createLabel(screen, WHITE, 210, 695, 145, 50, ("£" + str(apartmentCost)), RED, 15, False, False, True)
				if pressed == 4:
					createLabel(screen, WHITE, 630, 680, 150, 50, ("£" + str(powerCost)), RED, 15, False, False, True)
				if pressed == 5:
					createLabel(screen, WHITE, 630, 750, 150, 50, ("£" + str(waterCost)), RED, 15, False, False, True)
				if pressed == 6:
					createLabel(screen, WHITE, 625, 550, 150, 35, ("£" + str(roadCost)), RED, 15, False, False, True)
				if pressed == 7:
					createLabel(screen, WHITE, 180, 695, 30, 50, ("£" + str(houseUpgradeCost)), RED, 15, False, False, True)
				if pressed == 8:
					createLabel(screen, WHITE, 365, 695, 30, 50, ("£" + str(apartmentUpgradeCost)), RED, 15, False, False, True)
		except:
			IndexError
		return money

#function to determine what button has been pressed
def buttonDeterminer(x, y, depressed, screen):
	alreadypressed = False
	for pressed in range(len(depressed)):
		if depressed[pressed] == 1:
			alreadypressed = True
	#If the button is not depressed (already clicked on) it will change to reflect it
	if alreadypressed == False:
		#Redraws the button to represent its depressed state
		if Locations[y][x] == 1:
			createButton(screen, GRAY, 25, 645, 155, 100, "House", RED, False, 1, True)
		if Locations[y][x] == 2:
			createButton(screen, GRAY, 210, 645, 155, 100, "Apartment", BLUE, False, 2, True)
		if Locations[y][x] == 3:
			createButton(screen, GRAY, 395, 645, 185, 100, "Demolish", CYAN, False, 3, True)
		if Locations[y][x] == 4:
			createButton(screen, GRAY, 630, 650, 145, 65, "Power", BLACK, False, 4, True)
		if Locations[y][x] == 5:
			createButton(screen, GRAY, 630, 720, 145, 65, "Water", BLACK, False, 5, True)
		if Locations[y][x] == 6:
			createButton(screen, GRAY, 625, 525, 145, 50, "Road", BLACK, False, 6, True)
		if Locations[y][x] == 7:
			createButton(screen, GRAY, 180, 645, 30, 100, "^", RED, False,  7, True)
		if Locations[y][x] == 8:
			createButton(screen, GRAY, 365, 645, 30, 100, "^", BLUE, False,  8, True)
		if Locations[y][x] == 9:
			pygame.QUIT
			quit(0)
		#Will change it to false to represent its depressed state
		depressed[(Locations[y][x] - 1)] = 1
	#If the button is depressed (already clicked on) it will change to reflect it
	else:
		#Redraws the button to represent its non depressed state
		if Locations[y][x] == 1:
			createButton(screen, WHITE, 25, 645, 155, 100, "House", RED, False, 1, True)
		if Locations[y][x] == 2:
			createButton(screen, WHITE, 210, 645, 155, 100, "Apartment", BLUE, False, 2, True)
		if Locations[y][x] == 3:
			createButton(screen, WHITE, 395, 645, 185, 100, "Demolish", CYAN, False, 3, True)
		if Locations[y][x] == 4:
			createButton(screen, WHITE, 630, 650, 145, 65, "Power", BLACK, False, 4, True)
		if Locations[y][x] == 5:
			createButton(screen, WHITE, 630, 720, 145, 65, "Water", BLACK, False, 5, True)
		if Locations[y][x] == 6:
			createButton(screen, WHITE, 625, 525, 145, 50, "Road", BLACK, False, 6, True)
		if Locations[y][x] == 7:
			createButton(screen, WHITE, 180, 645, 30, 100, "^", RED, False,  7, True)
		if Locations[y][x] == 8:
			createButton(screen, WHITE, 365, 645, 30, 100, "^", BLUE, False,  8, True)
		if Locations[y][x] == 9:
			pygame.QUIT
			quit(0)
		#Will change it to false to represent its non-depressed state
		depressed[(Locations[y][x] - 1)] = 0
	#Will return these variables to update them for the other functions
	return depressed

def variableCalc(screen, population, money, powerBalance, waterBalance, powerTiles, waterTiles):
	pygame.draw.rect(screen, WHITE, [625, 120, 165, 20])
	createLabel(screen, WHITE, 625, 125, 155, 10, ("£" + str(math.ceil(money))), BLACK, 25, False, False, False)
	#Updates the population variable
	pygame.draw.rect(screen, WHITE, [625, 170, 165, 25])
	createLabel(screen, WHITE, 625, 180, 155, 10, str(population), BLACK, 25, False, False, False)
	#Updates the power variable
	powerDemand = population * 0.1
	powerSupply = powerTiles * 100
	powerBalance = powerSupply - powerDemand
	pygame.draw.rect(screen, WHITE, [625, 225, 165, 25])
	if powerBalance > 0:
		createLabel(screen, WHITE, 625, 235, 155, 10, str(math.ceil(powerBalance)) + " Mwh", GREEN, 25, False, False, False)
	else:
		createLabel(screen, WHITE, 625, 235, 155, 10, str(math.ceil(powerBalance)) + " Mwh", RED, 25, False, False, False)
	#Updates the water variable
	waterDemand = population * 0.142
	waterSupply = waterTiles * 350
	waterBalance = waterSupply - waterDemand
	pygame.draw.rect(screen, WHITE, [625, 280, 165, 25])
	if waterBalance > 0:
		createLabel(screen, WHITE, 625, 290, 155, 10, str(math.ceil(waterBalance)) + " Kl", GREEN, 25, False, False, False)
	else:
		createLabel(screen, WHITE, 625, 290, 155, 10, str(math.ceil(waterBalance)) + " Kl", RED, 25, False, False, False)
	#Calculates Tax Income
	tax = (population * 0.0005)
	#Calculates Penalty for not fulfilling demand
	if powerBalance < 0:
		tax = tax * (powerSupply/powerDemand)
	if waterBalance < 0:
		tax = tax * (waterSupply/waterDemand)
	#Updates money variable
	money += tax
	#Returns the money variable
	return money

