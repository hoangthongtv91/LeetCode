class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        for i in range(len(arr)):
            x = list(arr[i])
            x.reverse()
            arr[i] = "".join(x)

        newStr = " ".join(arr)
        return newStr

    print(reverseWords("a", "my name is thong"))