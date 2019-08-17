from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = heights.copy()
        heights.sort()
        i = ans = 0
        while i < len(heights):
            if x[i] != heights[i]: ans += 1
            i += 1

        return ans

    print(heightChecker("a", [1,1,4,2,1,3]))
