class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic,ans= [],[]
        for i in range(len(mat)): dic.append((mat[i].count(1),i))
        dic.sort()
        for i in range(k): ans.append(dic[i][1])
        return ans