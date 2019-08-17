from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        s = text.split()
        for i in range(len(s) - 1):
            if s[i] == first and s[i + 1] == second:
                ans.append(s[i + 2])

        return ans