maxRed = 12
maxGreen = 13
maxBlue = 14

textFile = open('day2input.txt', 'r')
games = textFile.readlines()
validGames = 0
sumPower = 0

for game in games:
    [gameLabel, allPulls] = game.split(':')
    [start, gameId] = gameLabel.split(' ')
    pulls = allPulls.strip().split(';')
    valid = True
    # fewest cubes needed
    red = 0
    green = 0
    blue = 0
    for p in range(len(pulls)):
        count = ''
        for i in range(len(pulls[p])):
            if (pulls[p][i].isnumeric()):
                count += pulls[p][i]
            elif (pulls[p][i:i+3] == 'red'):
                i = i+3
                if int(count) > maxRed:
                    valid = False
                if int(count) > red:
                    red = int(count)
                count = ''
            elif (pulls[p][i:i+5] == 'green'):
                i = i+5
                if int(count) > maxGreen:
                    valid = False
                if int(count) > green:
                    green = int(count)
                count = ''
            elif (pulls[p][i:i+4] == 'blue'):
                i = i+4
                if int(count) > maxBlue:
                    valid = False
                if int(count) > blue:
                    blue = int(count)
                count = ''
    sumPower += (red*green*blue)
    print(f"gameId: {gameId} valid: {valid}")
    if valid:
        validGames += int(gameId)
print(f"valid Games: {validGames}")
print(f"sumPower: {sumPower}")
