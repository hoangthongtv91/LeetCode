class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        S = [0, 1, 1]
        for i in range(3, n + 1):
            S.append(S[i - 3] + S[i - 2] + S[i - 1])

        return S[i]