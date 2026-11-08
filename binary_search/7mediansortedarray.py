'''
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution should run in O(log(m+n)) time.
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


nums1 = [1,2]
nums2 = [3]
res = Solution().findMedianSortedArrays(nums1, nums2)
print(res)
