class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        subset=[]
        candidates.sort()

        def dfs(i,curr):
            total = sum(element for element in curr)
            if total == target:
                results.append(curr[:])
                return
            if i>= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i+1,curr)
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            curr.pop()
            dfs(i+1,curr)
        dfs(0,[])
        return results
        
        