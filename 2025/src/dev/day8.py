with open('2025/src/resources/day8_input.txt') as f:
    lines = [list(map(int, l.strip().split(','))) for l in f.readlines()]
top = 3
num_shortest_connections = 10

def euc_dist(x1,y1,z1,x2,y2,z2):
    return ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(0.5)

# triu pairwise min
pairwise_min = []
for i, (x1,y1,z1) in enumerate(lines[:-1]):
    for j, (x2,y2,z2) in enumerate(lines):
        if i >= j:
            continue
        dist = euc_dist(x1,y1,z1,x2,y2,z2)
        pairwise_min.append([i, j, dist])

pairwise_sort = sorted(pairwise_min, key=lambda item: item[2]) # for pair in pairwise_min ]
# make circuits
circuits = []
# pairwise_sort[row_sort_pairwise]
circuits.append({pairwise_sort[0][0], pairwise_sort[0][1]})
circ_index_list = [-i for i in range(len(lines))]

for i,j,dist in pairwise_sort[:num_shortest_connections]:
    found = False
    print(i,j,dist)
    if circ_index_list[i] > 0 and circ_index_list[j] > 0 and circ_index_list[j] != circ_index_list[i]: #merge
        circuits[circ_index_list[i]].update(circuits[circ_index_list[j]])
        circuits.pop(circ_index_list[j])
        print(circuits)
        continue
    for k,circ in enumerate(circuits):
        if (i in circ) or (j in circ):
            circ.add(i)
            circ.add(j)
            circ_index_list[i] = k
            circ_index_list[j] = k
            found = True
    if not found:
        circuits.append({i, j})
        circ_index_list[i] = len(circuits)
        circ_index_list[j] = len(circuits)
    print(circuits)


# merge overlapping circuits until no overlaps remain
# merged = True
# while merged:
#     merged = False
#     i = 0
#     while i < len(circuits):
#         j = i + 1
#         while j < len(circuits):
#             if any(item in circuits[j] for item in circuits[i]): # circuits[i] & circuits[j]
#                 circuits[i].update(circuits[j]) # circuits[i] |= circuits[j]
#                 circuits.pop(j)
#                 merged = True
#             else:
#                 j += 1
#         i += 1
# print(circuits)

# merge_circuits = []
# for i, circ_i in enumerate(circuits):
#     for j, circ_j in enumerate(circuits):
#         if any(item in circ_j for item in circ_i):
#             circ_i.update(set_j)

top_len = sorted([len(circ) for circ in circuits], reverse=True)
x = top_len[0]
for i in top_len[1:top]:
    x *= i
print(x)