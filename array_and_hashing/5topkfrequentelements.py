from typing import List
'''
Given an integer array nums and an integer k, return the k most frequent elements 
within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a occurrence map
        frequency_map = {}

        # go through nums
        for num in nums:
            # store each elements occurence in map
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        # convert map to array
        frequency_arr = list(frequency_map.items())

        # get the highest occurrence items uptil k items
        frequency_arr.sort(key=lambda pair: pair[1], reverse=True)

        count_list = [pair[0] for pair in frequency_arr]

        return count_list[:k]


nums = [1,2,2,3,3,3]
k = 2
s = Solution()
res = s.topKFrequent(nums, k)
print(res)