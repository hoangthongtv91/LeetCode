from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        ans = []
        for x in A:
            if x in ans:
                return x
            else:
                ans.append(x)