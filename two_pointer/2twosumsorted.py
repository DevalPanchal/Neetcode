'''
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use sO(1) additional space.
'''
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            # decrease right pointer if target larger
            if numbers[left] + numbers[right] > target:
                right -=1  

            # increase left pointer if target is smaller
            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]





s = Solution().twoSum([1, 1, 2, 3, 4, 5], 5)

print(s)