"""
Scoring Points
1 for Rock
2 for Paper
3 for Scissors


0 if you lost
3 if the round was a draw
6 if you won

Rock Codes: A/X
Paper Codes: B/Y
Scissors Codes: C/Z

Rock defeats Scissors
Scissors defeats Paper
Paper defeats Rock.

"""

winPointsDict = {    
    'You Lose': 0,
    'You Draw': 3,
    'You Win': 6
}

optionsPointsDict = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

rulesList = [
    ['Rock','Rock','You Draw'],
    ['Rock','Paper','You Win'],
    ['Rock','Scissors','You Lose'],
    ['Paper','Rock','You Lose'],
    ['Paper','Paper','You Draw'],
    ['Paper','Scissors','You Win'],
    ['Scissors','Rock','You Win'],
    ['Scissors','Paper','You Lose'],
    ['Scissors','Scissors','You Draw']
]

def decryptChoice(encryptedChoice: str):
    if encryptedChoice == "A" or encryptedChoice == "X":
        return "Rock"
    if encryptedChoice == "B" or encryptedChoice == "Y":
        return "Paper"
    if encryptedChoice == "C" or encryptedChoice == "Z":
        return "Scissors"
    return "Error"

def checkResult(opponentChoice: str, playerChoice: str):
    for result in rulesList:
        if result[0] == opponentChoice and result[1] == playerChoice:
            return result[2]

def pointCalc(opponentChoice: str, playerChoice: str):
    opponentChoiceDecrypted = decryptChoice(opponentChoice)
    playerChoiceDecrypted = decryptChoice(playerChoice)
    result=checkResult(opponentChoiceDecrypted,playerChoiceDecrypted)
    winPoints = winPointsDict[result]
    optionPoints = optionsPointsDict[playerChoiceDecrypted]
    total = winPoints + optionPoints
    return total

round=1
score=0

f = open("puzzle-input.txt","r")
lines = f.readlines()


for line in lines:
    line = line.replace('\n','')
    opponentChoice,playerChoice = line.split(' ')
    opponentChoiceDecrypted = decryptChoice(opponentChoice)
    playerChoiceDecrypted = decryptChoice(playerChoice)
    result=checkResult(opponentChoiceDecrypted,playerChoiceDecrypted)
    pointsWon = pointCalc(opponentChoice,playerChoice)
    score = score + pointsWon
    print(f'Round {round}: Opponent plays {opponentChoiceDecrypted} ({opponentChoice}), Player plays {playerChoiceDecrypted} ({playerChoice}) - Result: {result} | Points this round: {pointsWon} | Score: {score}')
    round+=1