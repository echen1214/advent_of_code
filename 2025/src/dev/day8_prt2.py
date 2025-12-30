with open('2025/src/resources/day8_input.txt') as f:
    lines = [list(map(int, l.strip().split(','))) for l in f.readlines()]

def euc_dist(x1,y1,z1,x2,y2,z2):
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

# triu pairwise min
pairwise_min = []
for i, (x1,y1,z1) in enumerate(lines[:-1]):
    for j, (x2,y2,z2) in enumerate(lines):
        if i >= j:
            continue
        dist = euc_dist(x1,y1,z1,x2,y2,z2)
        pairwise_min.append([i, j, dist])

pairwise_sort = sorted(pairwise_min, key=lambda item: item[2])
print(len(pairwise_sort))
## part 2
circuits = []
# circuits.append({pairwise_sort[0][0], pairwise_sort[0][1]})
circ_index_list = [-1 for _ in range(len(lines))]

for l, (i, j, dist) in enumerate(pairwise_sort):
    found = False
    # print(i,j,dist)
    if circ_index_list[i] != -1 and circ_index_list[j] != -1 and circ_index_list[i] != circ_index_list[j]:
        a = circ_index_list[i]
        b = circ_index_list[j]
        # merge into the smaller index to keep pop adjustments simple
        target, source = (a, b) if a < b else (b, a)
        circuits[target].update(circuits[source])
        # update indices for members of the popped circuit
        for node in circuits[source]:
            circ_index_list[node] = target
        circuits.pop(source)
        # decrement indices greater than source
        for k, idx in enumerate(circ_index_list):
            if idx > source:
                circ_index_list[k] -= 1
    else:
        for k,circ in enumerate(circuits):
            if (i in circ) or (j in circ):
                circ.add(i)
                circ.add(j)
                circ_index_list[i] = k
                circ_index_list[j] = k
                found = True
        if not found:
            circuits.append({i, j})
            new_idx = len(circuits)-1
            circ_index_list[i] = new_idx
            circ_index_list[j] = new_idx

    if len(circuits[0]) == len(lines):
        # print(circuits, circ_index_list)
        print(l, lines[i], lines[j], i, j )
        print(lines[i][0]*lines[j][0])
        break
