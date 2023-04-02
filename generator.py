import wordsorter as ws
import projecttools as pt
import timemodule as tm
import time

starttime = time.time()

formattedgrid = ""
wordlendict = ws.CreateWordLengthDict("words_alpha_short")
rawgrid = pt.generatePlayGrid(15, 15, 50)
acrosswords, fixedGrid = pt.FindPerfectWord(rawgrid, wordlendict)

for i, tile in enumerate(fixedGrid):
    formattedgrid += tile

print(formattedgrid)
print("Across: ", acrosswords)

tm.compareTime(starttime)