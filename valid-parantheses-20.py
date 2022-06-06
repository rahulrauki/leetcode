class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(","}":"{","]":"["}
        for i in s:
            if i in dic.values(): stack.append(i)
            elif i in dic.keys():
                if stack == [] or dic[i] != stack.pop():
                    return False
            else: return False
        return stack == []

#Using stack, where if its an opening bracket we append and if closing we check if the last added is a matching one (by pop)