class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        subset=[]
        def dfs(i,curr):
            total = sum(element for element in curr)
            if total == target:
                results.append(curr[:])
                return
            if i>= len(nums) or total > target:
                return
            curr.append(nums[i])
            dfs(i,curr)
            curr.pop()
            dfs(i+1,curr)
        dfs(0,[])
        return results
        