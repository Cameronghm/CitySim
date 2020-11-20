import pygame
import random
from Setup import *

#function to draw a button with text
def createButton(screen, buttoncolour, x, y, width, height, text, textcolour, first, button, border):
    #Sets the font for the text that will be added over the button
    font = pygame.font.SysFont("Roboto", 40)
	#Draws a rectangle on the window with the size specified
    pygame.draw.rect(screen, buttoncolour, [x, y, width, height])
	#Creates the text based on the text variable and colour variable
    text = font.render(text, True, textcolour)
	#Places the text object on top of the rectangle object and centres it
    screen.blit(text, (x+((width-text.get_rect().width)/2),y+((height-text.get_rect().height)/2)))
	#If this is the first time that the button is being created
    if first == True:
		#Will assign the values to the location array
        objectLocations(x, y, width, height, button)
    else:
        if button == 1:
            createLabel(screen, WHITE, 25, 695, 145, 50, ("£" + str(houseCost)), BLACK, 15, False, False, True)
        if button == 2:
            createLabel(screen, WHITE, 210, 695, 145, 50, ("£" + str(apartmentCost)), BLACK, 15, False, False, True)
        if button == 4:
            createLabel(screen, WHITE, 630, 680, 150, 50, ("£" + str(powerCost)), BLACK, 15, False, False, True)
        if button == 5:
            createLabel(screen, WHITE, 630, 750, 150, 50, ("£" + str(waterCost)), BLACK, 15, False, False, True)
        if button == 6:
            createLabel(screen, WHITE, 625, 550, 150, 35, ("£" + str(roadCost)), BLACK, 15, False, False, True)
        if button == 7:
            createLabel(screen, WHITE, 180, 695, 30, 50, ("£" + str(houseUpgradeCost)), BLACK, 15, False, False, True)
        if button == 8:
            createLabel(screen, WHITE, 365, 695, 30, 50, ("£" + str(apartmentUpgradeCost)), BLACK, 15, False, False, True)
    if border == True:
        pygame.draw.rect(screen, GRAY, [x, y , width, height], 2)

def createLabel(screen, labelcolour, x, y, width, height, text, textcolour, fontsize, underline, bold, transparent):
    if transparent == True:
        transparent = -1
    if transparent == False:
        transparent = 0
    #Sets the font for the text
    font = pygame.font.SysFont("Roboto", fontsize)
	#Draws a rectangle on the window with the size specified
    pygame.draw.rect(screen, labelcolour, [x, y, width, height], transparent)
    #Creates an underline if underline = True
    font.set_underline(underline)
    font.set_bold(bold)
    #Creates the text based on the text variable and colour variable
    text = font.render(text, True, textcolour)
	#Places the text object on top of the rectangle object and centres it
    screen.blit(text, (x+((width-text.get_rect().width)/2),y+((height-text.get_rect().height)/2)))
#A function to set values in the location array
def objectLocations(x, y, width, height, button):
	#As arrays start from 0, I have subtracted 1 from each variable
	starty = y - 1
	endy = y + height - 1
	startx = x - 1 
	endx = x + width - 1
	#This will cycle through the location array to set the correct values
	while endy >= starty:
		tempx = endx
		while tempx >= startx:
			Locations[endy][tempx] = button
			tempx -= 1
		endy -= 1

def roadDecider(row, column):
	tilesaround = [0,0,0,0]
	if row == 0 and column == 0:
		tilesaround[0] = 3
		tilesaround[1] = 3
		tilesaround[2] = Land[row][column+1]
		tilesaround[3] = Land[row+1][column]
	elif row == 9 and column == 0:
		tilesaround[0] = Land[row-1][column]	
		tilesaround[1] = 3
		tilesaround[2] = Land[row][column+1]
		tilesaround[3] = 3
	elif row == 0 and column == 9:
		tilesaround[0] = 3
		tilesaround[1] = Land[row][column-1]
		tilesaround[2] = 3
		tilesaround[3] = Land[row+1][column]
	elif row == 9 and column == 0:
		tilesaround[0] = Land[row-1][column]
		tilesaround[1] = 3
		tilesaround[2] = Land[row][column+1]
		tilesaround[3] = 3
	elif row == 0  and column != 0:
		tilesaround[0] = 3
		tilesaround[1] = Land[row][column-1]
		tilesaround[2] = Land[row][column+1]
		tilesaround[3] = Land[row+1][column]
	elif row == 9 and column != 0:
		tilesaround[0] = Land[row-1][column]
		tilesaround[1] = Land[row][column-1]
		tilesaround[2] = Land[row][column+1]
		tilesaround[3] = 3
	elif row != 0  and column == 0:
		tilesaround[0] = Land[row-1][column]
		tilesaround[1] = 3
		tilesaround[2] = Land[row][column+1]
		tilesaround[3] = Land[row+1][column]
	elif row != 0  and column == 9:
		tilesaround[0] = Land[row-1][column]
		tilesaround[1] = Land[row][column-1]
		tilesaround[2] = 3
		tilesaround[3] = Land[row+1][column]
	else:
		tilesaround = [Land[row-1][column],Land[row][column-1],Land[row][column+1],Land[row+1][column]]
	top = False
	left = False
	right = False
	bottom = False
	if (tilesaround[0] != 0) and (tilesaround[0] != 1) and (tilesaround[0] != 2) and (tilesaround[0] != 7) and (tilesaround[0] != 8) and (tilesaround[0] != 9) and (tilesaround[0] != 10):
		top = True
	if (tilesaround[1] != 0) and (tilesaround[1] != 1) and (tilesaround[1] != 2) and (tilesaround[1] != 7) and (tilesaround[1] != 8) and (tilesaround[1] != 9) and (tilesaround[1] != 10):
		left = True
	if (tilesaround[2] != 0) and (tilesaround[2] != 1) and (tilesaround[2] != 2) and (tilesaround[2] != 7) and (tilesaround[2] != 8) and (tilesaround[2] != 9) and (tilesaround[2] != 10):
		right = True
	if (tilesaround[3] != 0) and (tilesaround[3] != 1) and (tilesaround[3] != 2) and (tilesaround[3] != 7) and (tilesaround[3] != 8) and (tilesaround[3] != 9) and (tilesaround[3] != 10):
		bottom = True
	if (top == True) and (left == True) and (right == False) and (bottom == False):
		road = "Top-LeftRoad.png"
	elif (top == True) and (left == True) and (right == True) and (bottom == False):
		road = "Top-Right-LeftRoad.png"
	elif (top == True) and (left == True) and (right == True) and (bottom == True):
		road = "RoundRoad.png"
	elif (top == True) and (left == False) and (right == False) and (bottom == True):
		road = "VerticalRoad.png"
	elif (top == True) and (left == False) and (right == True) and (bottom == False):
		road = "Top-RightRoad.png"
	elif (top == True) and (left == True) and (right == False) and (bottom == True):
		road = "Bottom-Left-TopRoad.png"
	elif (top == True) and (left == False) and (right == True) and (bottom == True):
		road = "Botton-Right-TopRoad.png"
	elif (top == False) and (left == True) and (right == False) and (bottom == True):
		road = "Botton-LeftRoad.png"
	elif (top == False) and (left == False) and (right == True) and (bottom == True):
		road = "Bottom-RightRoad.png"
	elif (top == False) and (left == True) and (right == True) and (bottom == True):
		road = "Botton-Left-RightRoad.png"
	elif (top == False) and (left == True) and (right == True) and (bottom == False):
		road = "HorizontalRoad.png"
	elif (top == False) and (left == False) and (right == False) and (bottom == False):
		road = "RoundRoad.png"
	elif (top == True) or (bottom == True):
		road = "VerticalRoad.png"
	elif (right == True) or (left == True):
		road = "HorizontalRoad.png"
	return road

#function that checks that the tiles are the right colour
def tileChecker(screen, population, power, water, powerTiles, waterTiles):
	population = 0
	powerTiles = 0
	waterTiles = 0
	for row in range(10):
		for column in range(10):
			#Empty Land
			if Land[row][column] == 0:
				colour = DARKGREEN
			#Draws the rectangle for each grid tile
				pygame.draw.rect(screen,
                             colour,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
			if Land[row][column] == 1:
				image = pygame.image.load('HousePoor.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				population += 50
			if Land[row][column] == 2:
				image = pygame.image.load('ApartmentPoor.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				population += 125
			if Land[row][column] == 4:
				image = pygame.image.load('Power.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				powerTiles += 1
			if Land[row][column] == 5:
				image = pygame.image.load('Water.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				waterTiles += 1
			if Land[row][column] == 6:
				image = pygame.image.load(roadDecider(row,column))
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
			if Land[row][column] == 7:
				image = pygame.image.load('HouseMiddle.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				population += 110
			if Land[row][column] == 8:
				image = pygame.image.load('HouseRich.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				population += 230
			if Land[row][column] == 9:
				image = pygame.image.load('ApartmentMiddle.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				population += 325
			if Land[row][column] == 10:
				image = pygame.image.load('ApartmentRich.png')
				screen.blit(image, [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
				population += 500
	return population, power, water, powerTiles, waterTiles