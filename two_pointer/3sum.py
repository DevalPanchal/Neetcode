'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output 
and the triplets in any order.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # go through [i+1:]
        for i in range(len(nums)):
            # if current number is greater than 0 then break
            if nums[i] > 0:
                break

            # if current index is beyond the first and current number is the same as the last one just skip a loop
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # we are going to loop over i + 1 (because i is also comparison)
            left = i + 1
            right = len(nums) - 1 # last element of list

            # two pointer approach
            while left < right:
                total = nums[left] + nums[right]

                print(f'{total} == {-nums[i]} | {nums[left]} | {nums[right]}')

                # if current total is the negative value of current number
                if total == -nums[i]:
                    # append the value
                    res.append([nums[i], nums[left], nums[right]])
                    # update the pointers
                    left += 1
                    right -= 1
                    # if current left pointer value is the same as left and left - 1 update pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                # if the total is more than the negative value of the current number than decrease right pointer
                elif total > -nums[i]:
                    right -= 1
                else:
                    left += 1

        return res




s = Solution().threeSum([-1,0,1,2,-1,-4])
# result [[-1,-1,2],[-1,0,1]]
print(s)