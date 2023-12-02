import sys

text_file = open('day1input.txt', 'r')
lines = text_file.readlines()
calibrations = []

for line in lines:
    num = []
    for c in range(0, len(line)):
        if (line[c].isnumeric()):
            num.append(line[c])
        elif (line[c:c+3] == 'one'):
            num.append('1')
        elif (line[c:c+3] == 'two'):
            num.append('2')
        elif (line[c:c+5] == 'three'):
            num.append('3')
        elif (line[c:c+4] == 'four'):
            num.append('4')
        elif (line[c:c+4] == 'five'):
            num.append('5')
        elif (line[c:c+3] == 'six'):
            num.append('6')
        elif (line[c:c+5] == 'seven'):
            num.append('7')
        elif (line[c:c+5] == 'eight'):
            num.append('8')
        elif (line[c:c+4] == 'nine'):
            num.append('9')
        elif (line[c:c+4] == 'zero'):
            num.append('0')
    calibrations.append(num[0]+num[len(num)-1])

final = 0
for cal in calibrations:
    final += int(cal)
print(final)
