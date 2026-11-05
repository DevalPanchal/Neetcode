'''
You are given an array of integers temperatures where temperatures[i] 
represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day 
before a warmer temperature appears on a future day. If there is no day in the 
future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
'''
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result



temperatures = [30,38,30,36,35,40,28]
s = Solution()
res = s.dailyTemperatures(temperatures)
print(res)

