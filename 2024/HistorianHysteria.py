text_file = open('day1input.txt', 'r')
lines = text_file.readlines()
left = []
right = []

for line in lines:
    pair = line.split()
    left.append(pair[0])
    right.append(pair[1])

leftsorted = sorted(left)
rightsorted = sorted(right)

difference = []

for i in range(leftsorted.size()):
    difference.append(abs(leftsorted[i]-rightsorted[i]))


sum = 0
for d in difference:
    sum += d

print(sum)
