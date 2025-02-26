text_file = open('2024/day1input.txt', 'r')
lines = text_file.readlines()
left = []
right = []

for line in lines:
    pair = line.split()
    left.append(int(pair[0]))
    right.append(int(pair[1]))

# part 1

# left_sorted = sorted(left)
# right_sorted = sorted(right)

# difference = []
# for i in range(0, len(left_sorted)):
#     difference.append(abs(left_sorted[i]-right_sorted[i]))

# sum = 0
# for d in difference:
#     sum += d

# part 2
score = []

left_set = set(left)

for i in left_set:
    count = right.count(i)
    score.append(count*i)

sum = 0
for i in score:
    sum += i


print(f"\n sum: {sum}\n")
