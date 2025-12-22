# split the string in half and compare the two

with open("2025/src/resources/day2_input.txt") as f:
    ranges = [range(*[int(n) if i==0 else int(n)+1 for i,n in enumerate(r.split('-'))]) for l in f.readlines() for r in l.strip().split(',')]

invalid_ids = []
for rang in ranges:
    for i in rang:
        id = str(i)
        len_id = len(id)
        inv = False
        spl_size = round(len_id/2)
        for j in range(len_id,1,-1):
            if len_id % j != 0:
                pass
            else:
                spl = int(len_id / j)
                id_check = [id[k*spl:(k+1)*spl] for k in range(int(len_id/spl))]
                if all(x==id_check[0] for x in id_check):
                    inv=True
        if inv:
            invalid_ids.append(i)

cum_sum = 0
for invalid in invalid_ids:
    cum_sum += invalid

print(cum_sum)
