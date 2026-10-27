'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # go through the array
        for i in range(len(nums)):
            # subtract 7 - current value
            complement = target - nums[i]
            # check if complement exists in seen
            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i


nums = [3,4,5,6]
target = 7
s = Solution()
res = s.twoSum(nums, target)
print(res)

