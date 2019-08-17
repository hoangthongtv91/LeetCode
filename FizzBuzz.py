from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 5 == 0:
                if i % 3 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Buzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))

        return ans

    print(fizzBuzz("a", 15))