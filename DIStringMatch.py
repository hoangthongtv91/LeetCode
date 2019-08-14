from typing import *


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i, j, ans = 0, len(S), []
        for s in S:
            if s == "I": ans.append(i); i += 1
            if s == "D": ans.append(j); j -= 1

        ans.append(i)

        return ans

