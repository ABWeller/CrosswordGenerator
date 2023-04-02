import random
import wordsorter as ws
import timemodule as tm
import time


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


#todo add the ability to change a tile to wall if there is only a "1 word" space
#todo across section almost works, except there is a problem counting near the edges
#todo change the across word search to ignore duplicate word
def FindPerfectWord(grid, wordsizedict):
    """
    iterates through grid to find down and across locations and a suitable word for each while respecting crossover
    create a dict? with the direction+number as key and word as value? but it needs a clue as reference too
    :param grid: list:
    :param wordsizedict: dict:
    :return: dict: acrosslist, downlist
    """
    acrosslist = {}
    tempwordstartindex = 0
    acrossiterations = 1
    words_added = [""]
    nextword = ""
    fixedgrid = grid

    # find across locations
    for tIndex, tile in enumerate(grid):

        # check if the tile is a blank with a wall-like tile that precedes it (first tile of a word)
        if tile == blank:
            if grid[tIndex -1] == wall or grid[tIndex -1] == "\n" or grid[tIndex -1] == None:
                tempwordstartindex = tIndex

        # check if the tile is a "word end" tile consisting of a wall like tile with a blank tile preceding it
        elif (tile == wall or tile == "\n") and tempwordstartindex >= 0:
            wordsize = tIndex - tempwordstartindex

            # word size finding logic goes here, replace wordsize in dict with actual word
            if wordsize > 1:

                # makes sure next word is not a duplicate
                # todo this needs a condition if there is no new word of a given size
                while nextword in words_added or nextword == None:
                    nextword = wordsizedict[wordsize][random.randint(0, len(wordsizedict[wordsize]) - 1)]
                acrosslist[acrossiterations] = [nextword, "hint"]
                words_added.append(nextword)

            else:
                # somehow fill in space with wall
                fixedgrid[tempwordstartindex] = wall
                # may need to lower across iterations by 1 to preserve the numbering
                acrossiterations -=1
                pass


            # reset variables
            acrossiterations += 1
            tempwordstartindex = -10
        else:
            pass

        #todo add the more complicated "down" word that are only viable if they have the right letters intersecting from across words





    return acrosslist, fixedgrid

def GetHints(wordsdict):
    """
    where will this get hints? internet search? scrape wikipedia?

    :param wordsdict: dict: raw dict with only words to lookup. format: {number: [word, hint]}
    :return: dict: updated dict with hints added
    """
    return



