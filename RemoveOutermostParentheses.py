class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        x, ans = 0, ""
        for i in S:
            if i == ")": x -= 1
            if x != 0: ans += i
            if i == "(": x += 1

        return ans
