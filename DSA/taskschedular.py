from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks).values()

        maxFreq = max(freq)
        count = list(freq).count(maxFreq)

        return max(len(tasks), (maxFreq - 1) * (n + 1) + count)
