class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lis = ''
        for tup in list(zip(*strs)):
            if len(set(tup)) == 1: lis+=tup[0]
            else: break
        return lis