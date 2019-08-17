from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            j = 0
            while j < len(arr1):
                if arr1[j] == i:
                    ans.append(arr1[j])
                    arr1.remove(arr1[j])
                else:
                    j += 1
        arr1.sort()
        ans += arr1
        return ans


    print(relativeSortArray("a", [2,2,2,3,5], [2,5]))