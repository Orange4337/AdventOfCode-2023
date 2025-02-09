textFile = open('day3input.txt', 'r')
lines = textFile.readlines()
number = '1234567890'
notSymbol = '1234567890.'
partSum = 0
symNum = []
partSum2 = 0


def adjacent(line, start, end):
    a = False
    for j in range(start-1, end+1):
        if j < 0:
            j = j+1
        if not (j > len(lines[line])-2):
            if line < len(lines)-1:
                if not ((lines[line+1][j] in notSymbol)):
                    symNum.append([line+1, j, int(lines[line][start:end])])
                    a = True
            if line > 0:
                if not (lines[line-1][j] in notSymbol):
                    symNum.append([line-1, j, int(lines[line][start:end])])
                    a = True
            if not (lines[line][j] in notSymbol):
                symNum.append([line, j, int(lines[line][start:end])])
                a = True
    return a


for line in range(len(lines)):
    start = 0
    end = 0
    i = 0
    # i needed to use a while because the for loops don't allow outside increments
    while i < len(lines[line]):
        if lines[line][i] in number:
            start = i
            end = i+1
            num = True
            while num:
                if lines[line][end] in number:
                    end += 1
                else:
                    num = False
            if (adjacent(line, start, end)):
                partSum += int(lines[line][start:end])
                # part1 debug print
                # print(
                #     f"line: {line+1} start: {start} end: {end} length: {len(lines[line])}")
                # print(f"part number: {lines[line][start:end]}")
            i = end
        i += 1
print(f"partSum: {partSum}")
for x in range(len(symNum)):
    for y in range(x+1, len(symNum)):
        if (symNum[x][0:2] == symNum[y][0:2]):
            # part 2 debug print
            # print(f"match {symNum[x]} {symNum[y]}")
            partSum2 += symNum[x][2]*symNum[y][2]
print(f"partSum2: {partSum2}")
