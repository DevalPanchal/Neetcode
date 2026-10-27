'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}

        # go through every single word in strs
        for word in strs:
            # sort the word
            sorted_word = "".join(sorted(word))

            # is the sorted word in already seen then append then word to that map
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]

        return list(word_map.values())


strs = ["act","pots","tops","cat","stop","hat"]
s = Solution()
res = s.groupAnagrams(strs)
print(res)
