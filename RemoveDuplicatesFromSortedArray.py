from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s1 = []
        i = 0
        while i < len(nums):
            if s1.__contains__(nums[i]):
                nums.remove(nums[i])
            else:
                s1.append(nums[i])
                i += 1
