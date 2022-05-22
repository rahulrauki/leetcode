# Runtime 1162ms ; Memory 14MB
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        if len(s) >= 1 and len(s) <= 1000:
            for i in range(len(s)):
                self.substrsplitter(s, i+1)
            return self.count
            
    def substrsplitter(self, string, indp1):
        for i in range(len(string)):
            if not i+indp1 <= len(string) :
                break
            if self.isPalindrome( string[i:i+indp1] ): self.count += 1 
        
    def isPalindrome(self, string):
        if string == string[::-1]:
            return True