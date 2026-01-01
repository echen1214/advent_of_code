with open("2025/src/resources/day9_input.txt") as f:
    lines = [list(map(int, l.strip().split(','))) for l in f.readlines()]

max_area = 0
# final_xy
for i, (x1,y1) in enumerate(lines):
    for x2,y2 in lines[i+1:]:
        area = abs(x1-x2+1)*abs(y1-y2+1)
        if area > max_area:
            max_area = area
            final_xy = ((x1,y1), (x2,y2))

print(final_xy, max_area)