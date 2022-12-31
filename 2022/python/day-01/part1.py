

import pprint
import string

elfcount = 1
calorieDict = dict()
totalCals = 0

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

pprint.pprint(calorieDict)

max_key = max(calorieDict, key=calorieDict.get)
max_val = calorieDict[max_key]
print(f'Elf {max_key} has the highest value of {max_val}')