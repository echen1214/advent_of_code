with open('2025/src/resources/day6_input.txt') as f:
    lines = [f.strip('\n') for f in f.readlines()]
operator = lines[-1].split()

print(lines)
def apply_operator(prev_value, curr_value, char):
    if char == "*":
        return int(prev_value) * int(curr_value)
    if char == "+":
        return int(prev_value) + int(curr_value)

count = 0
prev_value = ""
problem_count = len(operator)-1
for j in range(len(lines[0])-1,-1,-1):
    operator_char = operator[problem_count]
    value = ""
    for i in range(0, len(lines[0:-1])):
        value += lines[i][j]

    print(value)
    if value == " "*len(lines[0:-1]):
        problem_count -= 1
        count += prev_value
        print("out", prev_value)
        prev_value = ""
    elif not prev_value == "":
        prev_value = apply_operator(prev_value, value, operator_char)
    else:
        prev_value = value
count += prev_value
print("out", prev_value)
print(count)

# for loop over columns
# for loop over all rows
# load first value into columns
# 
# if all space then add to count
