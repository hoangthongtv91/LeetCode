from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        listS = list(S)
        arr = []
        ans = []
        for i in range(len(listS)):
            if listS[i] == C: arr.append(i)

        for i in range(len(listS)):
            ans.append(min(abs(i - location) for location in arr))

        return ans

    print(shortestToChar("a", "loveleetcode", "e"))
