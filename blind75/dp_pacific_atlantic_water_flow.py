class Solution:
    def pacific_atlantic_water_flow(self, heights):
        row = len(heights)
        col = len(heights[0])
        result = []

        dp = [[None for _ in range(col)] for _ in range(row)]
        dp[0][col-1] = True
        dp[row-1][0] = True

        for i in range(row):
            for j in range(col):
                if self.canReachPacific(
                    heights, i, j, row, col, [[False for _ in range(col)] for _ in range(row)], dp) and self.canReachAtlantic(
                        heights, i, j, row, col, [[False for _ in range(col)] for _ in range(row)], dp):
                    result.append([i,j])
        return result

    def isAtlantic(self, i, j, row, col):
        if i == row-1 or j == col-1:
            return True

    def isPacific(self, i, j):    
        if i == 0 or j == 0:
            return True
    
    def canReachPacific(self, heights, i, j, row, col, visited, dp, height=float('inf')):
        if i < 0 or i >= row or j < 0 or j >= col:
            return False
        
        if visited[i][j]:
            return False

        if dp[i][j]:
            return True
        
        if heights[i][j] > height:
            return False

        if self.isPacific(i, j):
            return True

        visited[i][j] = True
        if self.canReachPacific(
            heights, i+1, j, row, col, visited, dp, heights[i][j]) or self.canReachPacific(
                heights, i-1, j, row, col, visited, dp, heights[i][j]) or self.canReachPacific(
                    heights, i, j+1, row, col, visited, dp, heights[i][j]) or self.canReachPacific(
                        heights, i, j-1, row, col, visited, dp, heights[i][j]):
            dp[i][j] = True
            return True
        visited[i][j] = False
        return False
    
    def canReachAtlantic(self, heights, i, j, row, col, visited, dp, height=float('inf')):
        if i < 0 or i >= row or j < 0 or j >= col:
            return False
        
        if visited[i][j]:
            return False
        
        if heights[i][j] > height:
            return False        
        
        if self.isAtlantic(i, j, row, col):
            return True

        visited[i][j] = True
        if self.canReachAtlantic(
            heights, i+1, j, row, col, visited, heights[i][j]) or self.canReachAtlantic(
                heights, i-1, j, row, col, visited, heights[i][j]) or self.canReachAtlantic(
                    heights, i, j+1, row, col, visited, heights[i][j]) or self.canReachAtlantic(
                        heights, i, j-1, row, col, visited, heights[i][j]):
            return True
        visited[i][j] = False
        return False        
    

# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
if __name__ == '__main__':
    s = Solution()
    print(s.pacific_atlantic_water_flow([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]))
    print(s.pacific_atlantic_water_flow([[1]]))