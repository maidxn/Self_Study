class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        coors = set()
        ROWS, COLUMNS = len(board), len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r, c) in coors or r < 0 or c < 0 or r == ROWS or c == COLUMNS or word[i] != board[r][c]:
                return False
            coors.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            coors.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r,c,0):
                    return True
        return False