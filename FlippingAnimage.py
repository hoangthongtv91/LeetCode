from typing import *


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()

        for i in A:
            for n,j in enumerate(i):
                if j == 1:
                    i[n] = 0
                else:
                    i[n] = 1
        return A