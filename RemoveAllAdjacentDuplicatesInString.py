class Solution:
    def removeDuplicates(self, S: str) -> str:
        listS = list(S)
        i = 0
        while i < len(listS) - 1:
            if listS[i] == listS[i+1]:
                del listS[i]
                del listS[i]
                if i > 0: i -= 1
            else: i += 1

        return "".join(listS)