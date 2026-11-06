'''
You are given an integer array piles where piles[i] is the 
number of bananas 
in the ith pile. You are also given an integer h, which 
represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. 
Each hour, you may choose a pile of bananas and eats k bananas 
from that pile. If the pile has less than k bananas, you may 
finish eating the pile but you can not eat from another pile 
in the same hour.

Return the minimum integer k such that you can eat all the 
bananas within h hours.
'''
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallestSpeed = 1
        largestSpeed = max(piles)

        while smallestSpeed < largestSpeed:
            mid = (smallestSpeed + largestSpeed) // 2

            hours = sum(math.ceil(pile/mid) for pile in piles)

            if hours <= h:
                # mid works, but a slower speed might too
                largestSpeed = mid 
            else:
                # mid is too slow, so the answer is faster
                smallestSpeed = mid + 1

        return smallestSpeed


piles = [1,4,3,2]
h = 9
res = Solution().minEatingSpeed(piles, h)

print(res)
