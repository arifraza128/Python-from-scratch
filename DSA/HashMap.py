nums = [1, 2, 2, 3, 1, 2]

freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1

print(freq)
