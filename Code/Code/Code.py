#Importing the libraries I need for the project
import pygame
#Importing all the variables and functions from Setup.py
from Setup import *
from DrawBandO import *
from GameMechanics import *
import time

#Initiates pygame library
pygame.init()
#Sets the screen to the right size and title
screen = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption(WINDOWTITLE)
#Loops until the user clicks the close button on the window
done = False
#Used to manage how fast the screen updates
clock = pygame.time.Clock()
#
#--------------------KEY--------------------
#Create Label --> Space | Background Colour | x Start | y Start | Width | Height | Text | Text Colour | Font Size | Underline | Bold | Transparent
#Create Button --> Space | Button Colour | x Start | y Start | Width | Height | Button Text | Text Colour | First | Button Number | Border
#Draw.Rect --> Space | Background Colour | x Start | y Start | Width | Height | Nothing = fill in, 2 = border with no fill
#-------------------------------------------

#--------------------Main Grid Box--------------------
pygame.draw.rect(screen, WHITE, [0,0, 605, 605], 2)
#--------------------Statistics Box--------------------
#Border 1 for Statistics Box
pygame.draw.rect(screen, WHITE, [605,55, 195,550], 2)
#Border 2 for Statistics Box
pygame.draw.rect(screen, GRAY, [610,60, 185,540], 2)
#Border 3 for Statistics Box
pygame.draw.rect(screen, WHITE, [615,65, 175,530])
#Statistics Box Label
createLabel(screen, WHITE, 625, 65, 155, 30, "Statistics", BLACK, 30, True, True, False)
#Money Label and Counter in Statistics Box
createLabel(screen, WHITE, 625, 100, 155, 10, "Money", BLACK, 25, False, False, False)
createLabel(screen, WHITE, 625, 125, 155, 10, ("£" + str(money)), BLACK, 25, False, False, False)
#Population Label and Counter in Statistics Box
createLabel(screen, WHITE, 625, 155, 155, 10, "Population", BLACK, 25, False, False, False)
createLabel(screen, WHITE, 625, 180, 155, 10, str(population), BLACK, 25, False, False, False)
#Power Label and Counter in Statistics Box
createLabel(screen, WHITE, 625, 210, 155, 10, "Power Balance", BLACK, 25, False, False, False)
createLabel(screen, WHITE, 625, 235, 155, 10, str(powerBalance) + " Kwh", BLACK, 25, False, False, False)
#Water Label and Counter in Statistics Box
createLabel(screen, WHITE, 625, 265, 155, 10, "Water Balance", BLACK, 25, False, False, False)
createLabel(screen, WHITE, 625, 290, 155, 10, str(waterBalance) + " Kl", BLACK, 25, False, False, False)
#Road Label and Button
createButton(screen, WHITE, 625, 525, 145, 50, "Road", BLACK, True, 6, True)
createLabel(screen, WHITE, 625, 550, 150, 35, ("£" + str(roadCost)), BLACK, 15, False, False, True) 
#Time Label
createLabel(screen, WHITE, 625, 315, 155, 20, "Time left" , BLACK, 25, False, False, False)
#--------------------Utility Box--------------------
#Border 1 for Utilities Box
pygame.draw.rect(screen, WHITE, [605,605, 195,195], 2)
#Border 2 for Utilities Box
pygame.draw.rect(screen, GRAY, [610,610, 185,185], 2)
#Border 3 for Utilities Box
pygame.draw.rect(screen, WHITE, [615,615, 175,175])
#Utility Box Label
createLabel(screen, WHITE, 625, 615, 155, 30, "Utilities", BLACK, 30, True, True, False)
#Utility Buttons
#Power Button
createButton(screen, WHITE, 630, 650, 145, 65, "Power", BLACK, True, 4, True)
#Water Button
createButton(screen, WHITE, 630, 720, 145, 65, "Water", BLACK, True, 5, True)
#Labels Underneath the Utility Buttons
createLabel(screen, WHITE, 630, 680, 150, 50, ("£" + str(powerCost)), BLACK, 15, False, False, True)
createLabel(screen, WHITE, 630, 750, 150, 50, ("£" + str(waterCost)), BLACK, 15, False, False, True)
#--------------------Residental Box--------------------
#Border 1 for Residental Box
pygame.draw.rect(screen, WHITE, [0,605, 605,195], 2)
#Border 2 for Residental Box
pygame.draw.rect(screen, GRAY, [5,610, 595,185], 2)
#Border 3 for Residental Box
pygame.draw.rect(screen, WHITE, [10,615, 585,175])
#Residental Box Label
createLabel(screen, WHITE, 10, 615, 585, 30, "Residental Buildings", BLACK, 30, True, True, False)
#Residental Buttons
createButton(screen, WHITE, 25, 645, 155, 100, "House", RED, True, 1, True)
createButton(screen, WHITE, 210, 645, 155, 100, "Apartment", BLUE, True, 2, True)
createButton(screen, WHITE, 395, 645, 185, 100, "Demolish", CYAN, True, 3, True)
#Upgrade Buttons
createButton(screen, WHITE, 180, 645, 30, 100, "^", RED, True,  7, True)
createButton(screen, WHITE, 365, 645, 30, 100, "^", BLUE, True,  8, True)
#Labels Underneath the Residental Buttons
createLabel(screen, WHITE, 25, 695, 145, 50, ("£" + str(houseCost)), BLACK, 15, False, False, True)
createLabel(screen, WHITE, 210, 695, 145, 50, ("£" + str(apartmentCost)), BLACK, 15, False, False, True)
createLabel(screen, WHITE, 180, 695, 30, 50, ("£" + str(houseUpgradeCost)), BLACK, 15, False, False, True)
createLabel(screen, WHITE, 365, 695, 30, 50, ("£" + str(apartmentUpgradeCost)), BLACK, 15, False, False, True)
#--------------------Quit Button--------------------
createButton(screen, WHITE, 605, 0, 195, 55, "Quit", RED, True, 9, True)

start = False
startTime = time.time()
beginTime = 0
#Will loop while done is false
while not done:
    #Will run if the user does something
	for event in pygame.event.get():
		if start == False:
			createLabel(screen, WHITE, 625, 365, 155, 20, "Press Enter to start the game" , BLACK, 15, False, False, False)
			if event.type == pygame.KEYDOWN:
				start = True
				beginTime = time.time() - startTime
				createLabel(screen, WHITE, 625, 365, 155, 20, "GAME STARTED!" , RED, 15, False, False, False)
		if start == True:
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#Gets x and y position of the mouse
				pos = pygame.mouse.get_pos()
				#Creates two variables to make the coordinates easier to work with
				x = pos[0]
				y = pos[1]
				if (round((time.time() - (startTime + beginTime)), 1) < 300):
					#If the user clicks inside the area for the game, it runs tileDeterminer
					if (x <= 600) and (y <= 600):
						#passes x, y coordinates and the status of which button is pressed
						money = tileDeterminer(x, y, depressed, money, screen, population)
					else:
						#changes the value of pressed and depressed depending on what button is pressed
						depressed = buttonDeterminer(x, y, depressed, screen)
	if (round((time.time() - (startTime + beginTime)), 1) < 300):
		#Updates the tiles in the grid
		population, powerBalance, waterBalance, powerTiles, waterTiles = tileChecker(screen, population, powerBalance, waterBalance, powerTiles, waterTiles)
		#Will correct the variables
		money = variableCalc(screen, population, money, powerBalance, waterBalance, powerTiles, waterTiles)
		#Will refresh the screen to display any changes
		pygame.display.flip()
	if round((time.time() - (startTime + beginTime)), 1) == 300.0:
		#Blank Screen and Music
		pygame.draw.rect(screen, WHITE, [0,0,800,800])
		pygame.display.flip()
		pygame.mixer.music.load('endGame.mp3')
		pygame.mixer.music.play()
		#Total box and score
		pygame.draw.rect(screen, GRAY, [100,100,600,600],2)
		pygame.draw.rect(screen, BLACK, [110,110,580,580],2)
		pygame.display.flip()
		time.sleep(1)
		createLabel(screen, WHITE, 110, 110, 580, 50, "CONGRATULATIONS", RED, 50, True, False, True)
		pygame.display.flip()
		time.sleep(1)
		createLabel(screen, WHITE, 110, 160, 580, 50, "Population:  " + str(population), BLACK, 40, False, False, True)
		pygame.display.flip()
		time.sleep(1)
		createLabel(screen, WHITE, 110, 210, 580, 50, "Money:  " + str(round(money)), BLACK, 40, False, False, True)
		pygame.display.flip()
		time.sleep(1)
		createLabel(screen, WHITE, 110, 260, 580, 50, "Rank:", BLACK, 40, True, False, True)
		pygame.display.flip()
		time.sleep(1)
		if money < 10000:
			image = pygame.image.load('Bronze.png')
			screen.blit(image, [300, 310, 580, 50])
		elif money < 50000:
			image = pygame.image.load('Silver.png')
			screen.blit(image, [300, 310, 580, 50])
		elif money > 100000:
			image = pygame.image.load('Gold.png')
			screen.blit(image, [300, 310, 580, 50])
		pygame.display.flip()
	if (start == True) and round((time.time() - (startTime + beginTime)), 1) < 300.0:
		createLabel(screen, WHITE, 625, 340, 155, 20, str(300 - round(time.time() - (startTime + beginTime))) , BLACK, 25, False, False, False)
	#Will refresh 60 times per second
	clock.tick(60)




