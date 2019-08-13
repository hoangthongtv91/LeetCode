from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for n,i in enumerate(A):
            A[n] = i * i

        A.sort()
        return A

