with open("2025/src/resources/day5_input.txt") as f:
    ingred, fresh = [], []
    swap = False
    for l in f.readlines():
        if l == '\n':
            swap = True
            continue
        if swap:
            fresh.append(l.strip())
        else:
            ingred.append(l.strip())

ing_set = set()
count = 0

# day5 test set
# for i in fresh:
#     found = False
#     for ing in ingred:
#         ing_range = list(map(int, ing.split('-')))
#         if (ing_range[0] < int(i) <= ing_range[1]) and not found:
#             count += 1
#             found = True
#             continue

ranges = [tuple(map(int, ing.split('-'))) for ing in ingred]
ranges.sort(key=lambda x: x[0])

# merge overlapping/adjacent ranges
merged = []
for s, e in ranges:
    if not merged or s > merged[-1][1] + 1:  # no overlap (use +1 if you want to treat adjacency as separate)
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

print(merged)  # merged, non-overlapping intervals
total_span = sum(e - s + 1 for s, e in merged)
print(total_span)

# merge overlapping/adjacent ranges
merged = []
for s, e in ranges:
    if not merged or s > merged[-1][1] + 1:  # no overlap (use +1 if you want to treat adjacency as separate)
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)

print(merged)  # merged, non-overlapping intervals
total_span = sum(e - s + 1 for s, e in merged)
print(total_span)