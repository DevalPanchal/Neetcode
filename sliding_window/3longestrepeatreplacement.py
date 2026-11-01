'''
You are given a string s consisting of only uppercase english 
characters and an integer k. You can choose up to k characters 
of the string and replace them with any other uppercase English 
character.

After performing at most k replacements, return the length of the 
longest substring which contains only one distinct character.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        counts = [0] * 26

        # go through the array
        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest


s = "XYYX"
k = 2
sol = Solution()
res = sol.characterReplacement(s, k)
print(res)