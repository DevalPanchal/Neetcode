'''
Given a string s, return true if it is a palindrome, 
otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # if left pointer is not an alphabet increase pointer
            while not s[left].isalnum():
                left += 1

            # if right pointer is not an alphabet decrease pointer
            while not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


s = Solution().isPalindrome("rac@@ecars!!!")
print(s)
