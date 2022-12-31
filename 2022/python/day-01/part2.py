
from operator import itemgetter
import pprint
import string

elfcount = 1
calorieDict = dict()
totalCals = 0
top_count = 3

f = open("puzzle-input.txt","r")
lines = f.readlines()

for line in lines:
    line = line.replace('\n','')
    if line == "":
      calorieDict[elfcount] = totalCals
      totalCals = 0
      elfcount+=1
    else:
        totalCals= totalCals + int(line)

calorieDict[elfcount] = totalCals

# pprint.pprint(calorieDict)

pprint.pprint(sorted(calorieDict.values()))

topDict = dict(sorted(calorieDict.items(), key = itemgetter(1), reverse = True)[:top_count])

pprint.pprint(topDict)

topTotal = sum(topDict.values())


print(f'The top three Elves are carrying {topTotal} total calories')