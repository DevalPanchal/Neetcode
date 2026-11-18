'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ 
times. You may assume that the majority element always exists in 
the array.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        occ = {}

        for num in nums:
            if num not in occ:
                occ[num] = 1
            else:
                occ[num] += 1

        for key, val in occ.items():
            if val > n / 2:
                return key

s = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
print(s)