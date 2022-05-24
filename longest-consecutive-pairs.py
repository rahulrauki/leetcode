#This problem is not a part of the leetcode but is a variation longest-valid-paranthesis-32
#  inputs are:
#  "(()"
#  ")()())"
#  ""
#  "))(()()()))()()()()()))"

#  expected output:
#  2
#  4
#  0
#  10

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        self.longest = 0
        stack = []
        for i in s:
            if i == "(":
                if len(stack) > 0 and stack[-1] == "(":
                     stack.clear()
                stack.append(i)
            elif i == ")":
                if len(stack) == 0: continue
                elif stack[-1] == ")":
                    if stack[-2] == "(":
                        self.longest = len(stack)
                    stack.clear()
                elif stack[-1] == "(":
                    stack.append(i)
                    self.longest = len(stack)
        return self.longest