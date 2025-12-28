with open('2025/src/resources/day7_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

beams = [0 for _ in range(len(lines[0]))]
for i,c in enumerate(lines[0]): 
    if c == "S":
        start = i
        beams[i] = 1
# print(beams, start)

def apply(beams, splitter):
    # count = 0
    beams_new = [b for b in beams]
    for i, (b,s) in enumerate(zip(beams, splitter)):
        if b > 0 and s == "^":
            beams_new[i] = 0
            beams_new[i-1] += beams[i]
            beams_new[i+1] += beams[i]
    return beams_new

count = 0
for line in lines[2::2]:
    beams = apply(beams, line)
    # print(line)
    # print("".join([str(b) for b in beams]))
    # count += sub_count

print(sum(beams))