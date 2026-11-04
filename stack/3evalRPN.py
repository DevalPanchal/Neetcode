'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero. 
'''
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # if the current token is not an operator
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                # if current token is an operator 
                right = stack.pop()
                left = stack.pop()
    
                if token == "+":
                    stack.append(left + right)
                if token == "-":
                    stack.append(left - right)
                if token == "*":
                    stack.append(left * right)
                if token == "/":
                    stack.append(int(left / right))

        return stack.pop()



        
tokens = ["1","2","+","3","*","4","-"]
s = Solution()
res = s.evalRPN(tokens)
print(res)
