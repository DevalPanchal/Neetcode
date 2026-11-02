'''
You are given an array of integers nums and an integer k. 
There is a sliding window of size k that starts at the left edge 
of the array. The window slides one position to the right until 
it reaches the right edge of the array.

Return a list that contains the maximum element in the window at 
each step.
'''
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        # q[-1] is index at back
        # q[0] is index at front

        for r in range(len(nums)):
            # remove smaller elements from back, then add r
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)

            # remove fronte if its outside the window
            if q[0] < r - k + 1:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])

        return res



            
        
nums = [1,2,1,0,4,2,6]
k = 3
s = Solution()
res = s.maxSlidingWindow(nums, k)
print(res)