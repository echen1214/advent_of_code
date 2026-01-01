with open("2025/src/resources/day9_input.txt") as f:
    lines = [list(map(int, l.strip().split(','))) for l in f.readlines()]

# print(sorted(lines, key=lambda x: x[0]))
# print(lines)
print(max(lines, key=lambda x: x[0]), min(lines, key=lambda x: x[0]))
print(max(lines, key=lambda x: x[1]), min(lines, key=lambda x: x[1]))

v_edge_list = [ (lines[i][0], lines[i+1][0]) for i, _ in enumerate(lines[:-1]) ] + [(lines[-1][0], lines[0][0])]
h_edge_list = [ (lines[i][1], lines[i+1][1]) for i, _ in enumerate(lines[:-1]) ] + [(lines[-1][1], lines[0][1])]

print(v_edge_list[:5], v_edge_list[-5:])
print(h_edge_list[:5], h_edge_list[-5:])
# thanks to hint from john pribyl and keith frost about checking the edges 
max_area = 0
for i, (x1,y1) in enumerate(lines):
    for x2,y2 in lines[i+1:]:
        # check if the xy coordinates of the rectangle intersect any other rectangle 
        invalid = False
        for v_edge, h_edge in zip(v_edge_list, h_edge_list):
            x_max, x_min = (x1, x2) if x1 >= x2 else (x2, x1)
            x_edge_max, x_edge_min = (v_edge[0], v_edge[1]) if v_edge[0] >= v_edge[1] else (v_edge[1], v_edge[0])

            y_max, y_min = (y1, y2) if y1 >= y2 else (y2, y1)
            y_edge_max, y_edge_min = (h_edge[0], h_edge[1]) if h_edge[0] >= h_edge[1] else (h_edge[1], h_edge[0])

            if x_edge_max == x_edge_min:
                if (x_max > x_edge_max > x_min) and (y_max > y_edge_min) and (y_min < y_edge_max):
                    invalid = True
                    break
            elif y_edge_max == y_edge_min:
                if y_max > y_edge_max > y_min and (x_max > x_edge_min) and (x_min < x_edge_max):
                    invalid = True
                    break                
        if not invalid:
            area = (abs(x1-x2)+1)*(abs(y1-y2)+1)
            if area > max_area:
                max_area = area
                final_xy = ((x1,y1), (x2,y2))

print(final_xy, max_area)

import matplotlib.pyplot as plt
import numpy as np

coords = np.asarray(lines)
x, y = coords[:, 0], coords[:, 1]

plt.figure(figsize=(6, 6))
plt.plot(x, y, '-o', lw=1.5, markersize=4)

rect = np.asarray([final_xy[0],(final_xy[0][0], final_xy[1][1]), final_xy[1], (final_xy[1][0], final_xy[0][1]), final_xy[0]])
print(rect)
plt.plot(rect[:,0], rect[:,1], '-o', lw=2.5, markersize=4, color="green")

# for i, (xi, yi) in enumerate(zip(x, y)):
#     plt.text(xi, yi, str(i), fontsize=8, ha='right', va='bottom')

plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vertices shape')
plt.savefig("day9_prt2.png")