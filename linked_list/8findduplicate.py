'''
You are given an array of integers nums containing n + 1 integers. 
Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every 
other integer appears at most once.

Return the repeated integer.
'''
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break


        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

nums = [1,2,3,2,2]
s = Solution().findDuplicate(nums)

print(s)