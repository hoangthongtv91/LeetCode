from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])

        return ans

