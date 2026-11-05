'''
You are given an array of integers heights where heights[i] 
represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed 
among the bars.
'''
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                idx = stack.pop()
                height = heights[idx]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea


heights = [7,1,7,2,2,4]
s = Solution()
res = s.largestRectangleArea(heights)
print(res)
        