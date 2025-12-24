import numpy as np

with open("2025/src/resources/day4_input.txt") as f:
    rolls = [list(l.strip()) for l in f.readlines()]

rolls = np.array(rolls)
def check_rolls(arr, x, y):
    def bound(arr, x, y, max_x, max_y):
        min_x, max_x = 0, max_x
        min_y, max_y = 0, max_y
        if (min_x <= x < max_x) & (min_y <= y < max_y):
            return arr[x,y]

    out = []
    for tup in (x-1,y-1), (x-1,y), (x-1,y+1), (x, y-1), (x, y+1), (x+1,y-1), (x+1,y), (x+1,y+1):
        out.append(bound(arr, tup[0], tup[1], arr.shape[0], arr.shape[1]))

    return np.array(out)

count = 0
for index, roll in np.ndenumerate(rolls):
    # print()
    if roll=="@" and sum(check_rolls(rolls, index[0], index[1])=="@") < 4:
        count += 1
print(count)

remove = True
count = 0
while remove:
    remove_roll = []
    remove = False
    for index, roll in np.ndenumerate(rolls):
        state = check_rolls(rolls, index[0], index[1])=="@"
        if (roll=="@") & (sum(state) < 4):
            remove_roll.append(index)
            remove=True
            count += 1
    # print(remove_roll)
    if remove_roll:
        rows, cols = zip(*remove_roll)
        rolls[list(rows), list(cols)] = "X"
    # print(count, rolls)

print(count)