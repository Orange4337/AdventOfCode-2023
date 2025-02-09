text_file = open('2024/day1input.txt', 'r')
lines = text_file.readlines()
left = []
right = []

for line in lines:
    pair = line.split()
    left.append(int(pair[0]))
    right.append(int(pair[1]))

leftsorted = sorted(left)
rightsorted = sorted(right)

difference = []

for i in range(0, len(leftsorted)):
    difference.append(abs(leftsorted[i]-rightsorted[i]))


sum = 0
for d in difference:
    sum += d

print(f"\n sum: {sum}\n")
