from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            for i in list(str(num)):
                if i == "0":
                    break
                if num % int(i) != 0:
                    break
            else:
                ans.append(num)

        return ans