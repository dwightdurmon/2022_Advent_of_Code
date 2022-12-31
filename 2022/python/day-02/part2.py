"""
Scoring Points
1 for Rock
2 for Paper
3 for Scissors


0 if you lost
3 if the round was a draw
6 if you won

Rock = A
Paper = B
Scissors = C

'You Lose' = X
'You Draw' = Y
'You Win' = Z

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
    if encryptedChoice == "A" :
        return "Rock"
    if encryptedChoice == "B":
        return "Paper"
    if encryptedChoice == "C":
        return "Scissors"
    if encryptedChoice == "X":
        return "You Lose"    
    if encryptedChoice == "Y":
        return "You Draw"    
    if encryptedChoice == "Z":
        return "You Win"    
    return "Error"

def encryptChoice(encryptedChoice: str):
    if encryptedChoice == "Rock" :
        return "A"
    if encryptedChoice == "Paper":
        return "B"
    if encryptedChoice == "Scissors":
        return "C"
    return "Error"

def selectOption(opponentChoice: str, roundResult: str):
    for result in rulesList:
        if result[0] == opponentChoice and result[2] == roundResult:
            return result[1]


def pointCalc(playerChoice: str, roundResult: str):
    playerChoiceDecrypted = decryptChoice(playerChoice)
    roundResultDecrypted = decryptChoice(roundResult)
    winPoints = winPointsDict[roundResultDecrypted]
    optionPoints = optionsPointsDict[playerChoiceDecrypted]
    total = winPoints + optionPoints
    print(f'Result: {roundResultDecrypted}({winPoints}) + {playerChoiceDecrypted}({playerChoice})({optionPoints}) = {total}')

    return total

round=1
score=0

f = open("puzzle-input.txt","r")
lines = f.readlines()


for line in lines:
    line = line.replace('\n','')
    opponentChoice,roundResult = line.split(' ')

    opponentChoiceDecrypted = decryptChoice(opponentChoice)
    roundResultDecrypted = decryptChoice(roundResult)
    
    playerChoice = selectOption(opponentChoiceDecrypted, roundResultDecrypted)
    playerChoiceDecrypted = encryptChoice(playerChoice)

    pointsWon = pointCalc(playerChoiceDecrypted,roundResult)
    score = score + pointsWon
    print(f'Round {round}: Opponent plays {opponentChoiceDecrypted} ({opponentChoice}), Player plays {playerChoiceDecrypted} ({playerChoice}) - Result: {roundResultDecrypted}({roundResult}) | Points this round: {pointsWon} | Score: {score}')
    #print(f'Round {round}: Opponent plays {opponentChoiceDecrypted} ({opponentChoice}), Player plays {playerChoiceEncrypted} - Result: {roundResultDecrypted}({roundResult}) | Points this round: {pointsWon} | Score: {score}')
    round+=1