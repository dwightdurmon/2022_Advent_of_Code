
def getPriority(letter: str):
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

# ================== MAIN ================

f = open("puzzle-input.txt","r")
lines = f.readlines()

sum = 0

lineCount=len(lines)
iterations = int(lineCount / 3)
print("Total Lines:", lineCount, "Iterations:", iterations)

for i in range(iterations):
    line1 = lines[0 + (3 * i)].replace('\n','')
    line2 = lines[1 + (3 * i)].replace('\n','')
    line3 = lines[2 + (3 * i)].replace('\n','')
    print("Line1:", line1)
    print("Line2:", line2)
    print("Line3:", line2)
    print("-----")
    commonItems = set(line1) & set(line2)  & set(line3)
    print("Common Items:", commonItems)
    for item in commonItems:
        sum = sum + getPriority(item)
        print("Letter:",item,"Priority:",getPriority(item), "Sum:", sum)
