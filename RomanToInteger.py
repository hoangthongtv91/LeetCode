class Solution:
    def romanToInt(self, s: str) -> int:
        x = 0
        s1 = list(s)
        for i in range(len(s1)):
            if s1[i] == "I":
                x += 1
                if i + 1 < len(s1) and (s1[i + 1] == "V" or s1[i + 1] == "X"):
                    x -= 1 * 2
            elif s1[i] == "V":
                x += 5
            elif s1[i] == "X":
                x += 10
                if i + 1 < len(s1) and (s1[i + 1] == "L" or s1[i + 1] == "C"):
                    x -= 10 * 2
            elif s1[i] == "L":
                x += 50
            elif s1[i] == "C":
                x += 100
                if i + 1 < len(s1) and (s1[i + 1] == "D" or s1[i + 1] == "M"):
                    x -= 100 * 2
            elif s1[i] == "D":
                x += 500
            elif s1[i] == "M":
                x += 1000
            else:
                x += 0
        return x