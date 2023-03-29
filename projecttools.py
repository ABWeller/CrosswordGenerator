import random

playGrid = []
blank = "_ "
wall = "X "
list_of_words = []
allowed_patterns = [[wall, wall, wall, blank], [blank, blank, wall, wall], [wall, wall, blank, wall],
                    [wall, blank, blank, wall], [blank,blank,blank,blank], [wall, wall, wall, wall], [], [blank],
                    [blank, wall], [wall, blank], [blank, wall, wall, wall], [blank,wall,blank,wall]]


def generatePlayGrid(gridWidth, gridHeight, wallchance = 25):
    """
    Generates a grid of gridWidth by gridHeight, attempting to add walls in such a way that they do not isolate any blanks
    :param gridWidth: int: width of grid
    :param gridHeight: int: height of grid
    :param wallchance: int: percent chance for a wall to be spawned
    :return: list: a generated grid separated by \n for each new row
    """
    grid = []
    previousLine = ["filler","filler","filler","filler","filler","filler","filler","filler","filler","filler","filler",
                    "filler","filler","filler","filler","filler","filler","filler","filler","filler","filler","filler"]
    adjacent_tiles = [wall,blank,wall,wall] # adjacent tiles are formatted like so: [topleft,top,topright,left] in relation to the current tile index

    for wIndex, w in enumerate(range(gridWidth)):
        for hIndex, h in enumerate(range(gridHeight)):

            # rerolls the number out of 100
            tileType = random.randint(0, 100)

            # creates a list of adjacent tiles based off the previous line and current tiles left index [topleft,top,topright,left]
            if len(previousLine) < 1 or len(adjacent_tiles) < 4:
                adjacent_tiles = [wall,blank,wall,wall]
            else:
                if hIndex >= len(previousLine) -1:
                    adjacent_tiles = [len(previousLine) -1, wall,wall, grid[-1]]
                else:
                    adjacent_tiles = (previousLine[hIndex:hIndex + 3])
                    try:
                        adjacent_tiles.append(grid[-1])
                    except Exception as e:
                        print(e , ": grid")

            # procedural grid logic based on nearby tiles
            if adjacent_tiles.count(wall) == 4:
                adjacent_tiles.append(wall)
            else:
                if adjacent_tiles not in allowed_patterns and tileType <= wallchance:
                    grid.append(wall)
                else:
                    grid.append(blank)

        # creates a snapshot of the previous line for reference during the next iteration
        previousLine = grid[wIndex * (gridHeight + 1):]

        # adds \n as a divider for every new row
        grid.append("\n")

    # makes sure the grid is the right size before returning (this should not be needed)
    if len(grid) == (gridWidth * gridHeight) + gridHeight:
        return grid
    else:
        return generatePlayGrid(gridWidth, gridHeight, wallchance)


def FindPerfectWord(grid):
    """
    iterates through grid to find down and across locations and a suitable word for each while respecting crossover
    create a dict? with the direction+number as key and word as value? but it needs a clue as reference too
    :param grid: list:
    :return:
    """
    return





formatted = ""
newGrid = generatePlayGrid(15, 15, 50)

for i, tile in enumerate(newGrid):
    formatted += tile

print(formatted)