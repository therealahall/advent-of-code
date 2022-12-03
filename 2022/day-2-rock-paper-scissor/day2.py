HANDS = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

SCORES = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
    "LOSE": 0,
    "DRAW": 3,
    "WIN": 6
}

def determineScore(opponent, player):
    if(HANDS[opponent] == HANDS[player]):
        return SCORES[HANDS[player]] + SCORES['DRAW']

    outcome = 'LOSE'
    match HANDS[opponent]:
        case 'ROCK':
            if(HANDS[player] == 'PAPER'):
                outcome = 'WIN'
        case 'PAPER':
            if(HANDS[player] == 'SCISSORS'):
                outcome = 'WIN'
        case 'SCISSORS':
            if(HANDS[player] == 'ROCK'):
                outcome = 'WIN'
    return SCORES[HANDS[player]] + SCORES[outcome]

file = open("input.txt", "r")
list = file.read().replace("\n", ",").split(",")
score = 0
for line in list:
    game = line.split(" ")
    score += determineScore(game[0], game[1])

print(score)