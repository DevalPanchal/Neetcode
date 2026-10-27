'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
'''

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create store to save num iterated through
        arr = set()

        # go through every number
        for num in nums:
            # if number is already in set then return True
            if num in arr:
                return True
            # otherwise keep adding to the set
            else:
                arr.add(num)

        return False


nums = [1, 1, 1]
s = Solution()
res = s.hasDuplicate(nums)
print(res)
