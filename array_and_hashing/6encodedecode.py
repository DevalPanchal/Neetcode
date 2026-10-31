'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded 
back to the original list of strings.
'''
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        '''
        convert list of string to string
        '''
        encoded_string = []
        for s in strs:
            encoded_string.append(f"{len(s)}#{s}")

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        '''
        convert string to original list of string
        '''
        res = []
        i = 0

        # go through string
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            # extract length of string
            length = int(s[i:j])

            # actual string starts after delimiter #
            start_idx = j + 1
            end_idx = start_idx + length
            res.append(s[start_idx:end_idx])

            i = end_idx

        return res


inp = ['Hello', 'world']
s = Solution()
encoded_string = s.encode(inp)
s = s.decode(encoded_string)

print(encoded_string, s)