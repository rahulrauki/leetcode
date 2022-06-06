#using a simple stack and permutations. Note, this was not accepted due to memory constraint. but works
from itertools import permutations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        perms = permutations(["(",")"]*n)
        combinations =set(["".join(i) for i in list(perms)])
        valid = []
        for comb in combinations:
            stack,flag = [],0
            for char in comb:
                if char == "(": stack.append(char)
                elif char == ")":
                    if stack == [] or stack.pop() != "(":
                        flag+=1
                        break
            if not flag: valid.append(comb)
        return valid