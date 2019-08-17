class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)
        bList = list(str(b)[2:])

        for i in range(len(bList)):
            if bList[i] == "1":
                bList[i] = "0"
            else:
                bList[i] = "1"

        return int("".join(bList), 2)