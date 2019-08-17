from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            x = stones.pop(0)
            y = stones.pop(0)
            if x - y != 0:
                stones.append(abs(x - y))

        if len(stones) == 1: return stones[0]
        else: return 0
