class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        x = 0
        j1 = list(J)
        s1 = list(S)
        for i in s1:
            if j1.__contains__(i):
                x += 1

        return x