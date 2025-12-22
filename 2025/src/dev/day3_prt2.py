import time
import numpy as np

with open("2025/src/resources/day3_input.txt") as f:
    bank = [l.strip() for l in f.readlines()]

sum = 0
t0 = time.perf_counter()
for b in bank:
    arr = [int(ch) for ch in b]
    out_str = ""
    dig0_ind = -1
    # print(b)
    for i in range(11,-1,-1):
        # print(arr[dig0_ind+1:-i])
        if i == 0:
            dig_new_ind = arr[dig0_ind+1:].index(max(arr[dig0_ind+1:]))
        else:
            dig_new_ind = arr[dig0_ind+1:-i].index(max(arr[dig0_ind+1:-i]))
        dig0_ind += dig_new_ind + 1
        # print(dig_new_ind, dig0_ind, i)
        out_str += str(arr[dig0_ind])
    sum += int(out_str)
    # print(out_str)
elapsed = time.perf_counter() - t0
print(f"solution 1: elapsed: {elapsed:.6f}s")
print(sum)

# solution 2
# t0 = time.perf_counter()
# sum = 0
# for b in bank:
#     arr = np.array([int(ch) for ch in b])
#     dig1_ind = np.argmax(arr[:-1])
#     dig2_ind = np.argmax(arr[dig1_ind+1:])
#     out = int(str(arr[dig1_ind]) + str(arr[dig1_ind+1+dig2_ind]))
#     sum+=out
# elapsed = time.perf_counter() - t0
# print(f"solution 1: elapsed: {elapsed:.6f}s")
# print(sum)