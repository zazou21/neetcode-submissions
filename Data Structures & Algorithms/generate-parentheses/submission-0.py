class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        stack=[]
        def backtrack(l,r):
            if l == r == n :
                result.append("".join(stack))
                return
            if l < n :
                stack.append("(")
                backtrack(l+1,r)
                stack.pop()
            if r < l:
                stack.append(")")
                backtrack(l,r+1)
                stack.pop()
        backtrack(0,0)
        return result



           

            
            
            

       

        