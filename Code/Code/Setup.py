import random

#Defining Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128,128,128)
GREEN = (50,205,50)
DARKGREEN = (0, 153, 51)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

#Setting the window size in pixels and the title of the window
WINDOWSIZE = [800,800]
WINDOWTITLE = "City Simulation"

#Defining grid sizes
WIDTH = 55
HEIGHT = 55
MARGIN = 5

#Setting starting variables for button depressed and button pressed
depressed = [0,0,0,0,0,0,0,0,0,0,0,0]
colour = WHITE

#Setup of game variables
money = 20000
population = 0
powerBalance = 0
waterBalance = 0
powerTiles = 0
waterTiles = 0

#Setup Button Values
houseCost = 1000
houseUpgradeCost = 2000
apartmentCost = 5000
apartmentUpgradeCost = 8000
powerCost = 2500
waterCost = 3000
roadCost = 500
clearCost = 0

#Creates function to create array for grid
def getLand():
    #Sets number of rows and columns in the grid
    ROWS = 10
    COLUMNS = 10
    #Creates a blank grid
    Land = []
    #Iterates through the rows, appending another array each time to represent each column
    for row in range(ROWS):
        Land.append([])
        #Iterates through each 2D array, setting each value to 0
        for column in range(COLUMNS):
            Land[row].append(0)
    Land = getRoad(Land)
    return Land

def getRoad(Land):
	row = random.randint(0,9)
	if (row == 0) or (row == 9):
		column = random.randint(0,9)
		Land[row][column] = 6
	else:
		column = random.randint(0,1)
		if column == 1:
			column = 9
		Land[row][column] = 6
	return Land

def getLocations():
	#Sets number of rows and columns in the grid
    ROWS = 800
    COLUMNS = 800
    #Creates a blank grid
    Locations = []
    #Iterates through the rows, appending another array each time to represent each column
    for row in range(ROWS):
        Locations.append([])
        #Iterates through each 2D array, setting each value to 0
        for column in range(COLUMNS):
            Locations[row].append(0)
    return Locations

#Generates land variable
Land = getLand()
Locations = getLocations()