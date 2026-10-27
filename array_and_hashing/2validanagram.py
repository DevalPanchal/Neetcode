'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # go through s and t and count occurrences of both
        map1 = {}
        map2 = {}

        for letter in range(len(s)):
            if s[letter] in map1:
                map1[s[letter]] += 1
            else:
                map1[s[letter]] = 1

        for letter in range(len(t)):
            if t[letter] in map2:
                map2[t[letter]] += 1
            else:
                map2[t[letter]] = 1

        # if occurrence of both are same return true otherwise false
        return map1 == map2
    
s = "racecar"
t = "carrace"
sol = Solution()
res = sol.isAnagram(s, t)
print(res)

