'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countsS1 = [0] * 26
        countsS2 = [0] * 26
        l = 0

        if len(s1) > len(s2):
            return False

        # go through s1 
        for i in range(len(s1)):
        # add count of each letter
            countsS1[ord(s1[i]) - 97] += 1
            countsS2[ord(s2[i]) - 97] += 1 # build window

        # go through s2
        for r in range(len(s1), len(s2)):
            if countsS1 == countsS2:
                return True

            countsS2[ord(s2[r]) - 97] += 1
            countsS2[ord(s2[l]) - 97] -= 1
            l += 1

        return countsS1 == countsS2


s1 = "abc"
s2 = "lecabee"
s = Solution()
res = s.checkInclusion(s1, s2)
print(res)


