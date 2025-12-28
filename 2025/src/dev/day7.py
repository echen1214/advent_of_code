with open('2025/src/resources/day7_input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

beams = [0 for _ in range(len(lines[0]))]
for i,c in enumerate(lines[0]): 
    if c == "S":
        start = i
        beams[i] = 1
print(beams, start)

def apply(beams, splitter):
    count = 0
    for i, (b,s) in enumerate(zip(beams, splitter)):
        if b == 1 and s == "^":
            beams[i] = 0
            beams[i-1] = 1
            beams[i+1] = 1
            count += 1
    return beams, count

count = 0
for line in lines[2::2]:
    beams, sub_count = apply(beams, line)
    print(line)
    print("".join([str(b) for b in beams]), sub_count)
    count += sub_count

print(count)
