with open('2025/src/resources/day6_input.txt') as f:
    lines = [f.strip().split() for f in f.readlines()]

print(lines)
def apply_operator(prev_value, curr_value, char):
    if char == "*":
        return int(prev_value) * int(curr_value)
    if char == "+":
        return int(prev_value) + int(curr_value)

count = 0
for j in range(len(lines[0])):
    value = lines[0][j]
    for i in range(1, len(lines[1:-1])+1):
        value = apply_operator(value, lines[i][j], lines[-1][j])
    count += value
    # print(count)

print(count)