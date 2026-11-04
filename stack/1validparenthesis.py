'''
You are given a string s consisting of the following characters: 
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # initalize bracket types (open/close)
        stack = []
        brackets = { '(': ')', '{': '}', '[': ']' }

        # go through s
        for bracket in s:
            # if current character is an open bracket then add to stack
            if bracket in brackets:
                stack.append(bracket)
            # if current character is a close bracket pop the corresponding bracket
            elif bracket in brackets.values():
                # is stack is not empty and there is an opening bracket
                if not stack:
                    return False

                # is current bracket the closing bracket for the last value in the stack
                if brackets[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False

        return not stack

s = "[()]"
sol = Solution()
res = sol.isValid(s)
print(res)
