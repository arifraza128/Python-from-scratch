class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]

        i2 = i3 = i5 = 0

        while len(ugly) < n:
            nextNum = min(
                ugly[i2] * 2,
                ugly[i3] * 3,
                ugly[i5] * 5
            )

            ugly.append(nextNum)

            if nextNum == ugly[i2] * 2:
                i2 += 1

            if nextNum == ugly[i3] * 3:
                i3 += 1

            if nextNum == ugly[i5] * 5:
                i5 += 1

        return ugly[-1]
