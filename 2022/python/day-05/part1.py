"""
Validation Initial Stack Configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 




"""
import pprint


vstack = {
    '1': ['N','Z'],
    '2': ['D','C','M'],
    '3': ['P']
}
"""
==============
Puzzle Initial Stack Configuration:

        [F] [Q]         [Q]        
[B]     [Q] [V] [D]     [S]        
[S] [P] [T] [R] [M]     [D]        
[J] [V] [W] [M] [F]     [J]     [J]
[Z] [G] [S] [W] [N] [D] [R]     [T]
[V] [M] [B] [G] [S] [C] [T] [V] [S]
[D] [S] [L] [J] [L] [G] [G] [F] [R]
[G] [Z] [C] [H] [C] [R] [H] [P] [D]
 1   2   3   4   5   6   7   8   9 

"""
pstack = {
    '1': ['B','S','J','Z','V','D','G'],
    '2': ['P','V','G','M','S','Z'],
    '3': ['F','Q','T','W','S','B','L','C'],
    '4': ['Q','V','R','M','W','G','J','H'],
    '5': ['D','M','F','N','S','L','C'],
    '6': ['D','C','G','R'],
    '7': ['Q','S','D','J','R','T','G','H'],
    '8': ['V','F','P'],
    '9': ['J','T','S','R','D'],
}

def getAction(line: str):
    _, itemCount, _, moveFrom, _, moveTo = line.split()
    return itemCount,moveFrom, moveTo

def getStackValues(stack: dict, stackNum: str):
    return stack[stackNum]

f = open("puzzle-input.txt","r")
lines = f.readlines()

stack = pstack

for line in lines:
    line = line.replace('\n','')
    itemCount,moveFrom, moveTo = getAction(line)
    moveFromValues = getStackValues(stack, moveFrom)
    moveToValues = getStackValues(stack, moveTo)
    # print('OldMoveFromValues:',moveFromValues)
    # print('OldMoveToValues:',moveToValues)
    # print("Move From: ",moveFromValues)
    # print("Move To: ", moveToValues)
    insertList=list()
    for i in range(int(itemCount)):
        item = moveFromValues.pop(0)
        # print(i,'Item:',item)
        insertList.insert(0,item)
    
    # print('InsertList:',insertList)
    moveToValues[0:0] = insertList
    # print('NewMoveFromValues:',moveFromValues)
    # print('NewMoveToValues:',moveToValues)
    
    
    stack[moveFrom] = moveFromValues
    stack[moveTo] = moveToValues
    # print("====")

# pprint.pprint(stack)
output=""
for item in stack:
    values=stack[item]
    output=output + values[0]
print(output)