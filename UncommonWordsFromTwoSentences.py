from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        setA = set()
        setB = set()

        duplicates = set()
        for word in A.split():
            if word not in setA:
                setA.add(word)
            else:
                duplicates.add(word)

        for word in B.split():
            if word not in setB:
                setB.add(word)
            else:
                duplicates.add(word)

        return (setA ^ setB) - duplicates