class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,idx):
            if idx >= len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[idx]:
                return False   
            if board[i][j] == word[idx]:
               temp = board[i][j]
               board[i][j] = "#"
               down=backtrack(i+1,j,idx+1)
               right=backtrack(i,j+1,idx+1)
               up=backtrack(i-1,j,idx+1)
               left=backtrack(i,j-1,idx+1)
               board[i][j] = temp
               return down or right or up or left
            
           
        for i in range(len(board)):
            for j in range(len(board[i])):
                result=backtrack(i,j,0)
                if result:
                    return True
        return False
                

        