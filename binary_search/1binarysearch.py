'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1

nums = [-1,0,2,4,6,8]
target = 4
s = Solution()
res = s.search(nums, target)
print(res)