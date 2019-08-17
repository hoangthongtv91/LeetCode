from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = [i for i in A[0]]

        for word in A[1:]:
            temp = []
            for char in word:
                if char in ans:
                    temp.append(char)
                    ans.remove(char)

            ans = temp

        return ans