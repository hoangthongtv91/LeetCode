from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        x = []
        for i in A:
            if i % 2 == 0:
                x.insert(0, i)
            else:
                x.append(i)

        return x