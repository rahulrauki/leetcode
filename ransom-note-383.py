from collections import Counter as C 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not C(ransomNote) - C(magazine)

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for i in ransomNote:
            try:
                mag.remove(i)
            except:
                return False
        return True