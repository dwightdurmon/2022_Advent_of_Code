
def getPriority(letter: str):
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def getCommmonItems(container1: str, container2: str):
    container1 = [*container1]
    container2 = [*container2]
    commonItems = set(container1) & set(container2)
    return commonItems

def splitHalf(line: str):
    line = line.replace('\n','')
    lineLength = len(line)
    if lineLength%2 == 0:
        container1 = line[0:lineLength//2]
        container2 = line[lineLength//2:]
    else:
        container1 = line[0:(lineLength//2+1)]
        container2 = line[(lineLength//2+1):]
    
    return container1, container2

# ================== MAIN ================

f = open("puzzle-input.txt","r")
lines = f.readlines()

sum = 0

for line in lines:
    container1, container2 = splitHalf(line)
    commonItems = getCommmonItems(container1, container2)
    print("Common Items:", commonItems)
    for item in commonItems:
        sum = sum + getPriority(item)
        print("Letter:",item,"Priority:",getPriority(item), "Sum:", sum)
