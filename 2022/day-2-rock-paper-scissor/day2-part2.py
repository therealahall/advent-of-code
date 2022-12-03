HANDS = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
}

OUTCOMES = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

SCORES = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
    "LOSE": 0,
    "DRAW": 3,
    "WIN": 6
}

def determineWinner(opponent, outcome):
    if(OUTCOMES[outcome] == "DRAW"):
        return SCORES[HANDS[opponent]] + SCORES[OUTCOMES[outcome]]

    match OUTCOMES[outcome]:
            case 'WIN':
                if(HANDS[opponent] == 'SCISSORS'):
                    playerHand = 'ROCK'
                elif(HANDS[opponent] == 'PAPER'):
                    playerHand = 'SCISSORS'
                else:
                    playerHand = 'PAPER'
            case 'LOSE':
                if(HANDS[opponent] == 'SCISSORS'):
                    playerHand = 'PAPER'
                elif(HANDS[opponent] == 'PAPER'):
                    playerHand = 'ROCK'
                else:
                    playerHand = 'SCISSORS'

    return SCORES[playerHand] + SCORES[OUTCOMES[outcome]]

file = open("input.txt", "r")
list = file.read().replace("\n", ",").split(",")
score = 0
for line in list:
    game = line.split(" ")
    score += determineWinner(game[0], game[1])

print(score)