from typing import List


class Solution:
    def findWords(self, words: List[str]):
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        def check(word):
            word = word.lower()
            if not word: return False
            if word[0] in row1: return row1 & set(word) == set(word)
            if word[0] in row2: return row2 & set(word) == set(word)
            if word[0] in row3: return row3 & set(word) == set(word)
            return False

        return filter(check, words)
