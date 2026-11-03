'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get count of all letters in t
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}
        have = 0
        need = len(countT)
        best = ""
        l = 0

        # go through s
        for r in range(len(s)):
            # grow r until window is valid
            c = s[r]
            window[c] = window.get(c, 0) + 1


            # did this letter just reach the amount t needs
            if c in countT and window[c] == countT[c]:
                have += 1

            # shrink while the window is valid
            while have == need:
                # save this window if its the smallest so far
                if best == "" or r - l + 1 < len(best):
                    best = s[l:r + 1]

                # remove the left letter
                left = s[l]
                window[left] -= 1

                # did removing it leave us with too few?
                if left in countT and window[left] < countT[left]:
                    have -= 1

                l += 1

        return best


s = "OUZODYXAZV"
t = "XYZ"
sol = Solution()
res = sol.minWindow(s, t)
print(res)