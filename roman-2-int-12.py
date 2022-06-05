class Solution: #If provided with valid inputs only, 52ms 13.9mb :: 82.11%, 75.78%
    def romanToInt(self, s: str) -> int:
        total,pos = 0,0
        for i in range(len(s)):
            if s[i]=="I" :
                total+=1
            elif s[i]=="V":
                if s[i-1] == "I" and pos != 0:total+=3
                else: total+=5
            elif s[i]=="X":
                if s[i-1] == "I" and pos != 0:total+=8
                else: total+=10
            elif s[i]=="L":
                if s[i-1] == "X" and pos != 0:total+=30
                else: total+=50
            elif s[i]=="C":
                if s[i-1] == "X" and pos != 0:total+=80
                else: total+=100
            elif s[i]=="D":
                if s[i-1] == "C" and pos != 0:total+=300
                else: total+=500
            else:
                if s[i-1] == "C" and pos != 0:total+=800
                else: total+=1000
            pos+=1
        return total