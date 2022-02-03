class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        H = len(heights)
        W = len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(j, i, visited, prevHeight):
            if j<0 or i<0 or j>=H or i>=W:
                return
            coor = (j, i)
            currentHeight = heights[j][i]
            if currentHeight < prevHeight or coor in visited:
                return
            visited.add(coor)
            dfs(j+1, i, visited, currentHeight)
            dfs(j-1, i, visited, currentHeight)
            dfs(j, i+1, visited, currentHeight)
            dfs(j, i-1, visited, currentHeight)
            
        for j in range(H):
            dfs(j, 0, pacific, float("-inf"))
            dfs(j, W-1, atlantic, float("-inf"))
            
        for i in range(W):
            dfs(0, i, pacific, float("-inf"))
            dfs(H-1, i, atlantic, float("-inf"))
            
        return [c for c in pacific.intersection(atlantic)]
