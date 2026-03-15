"""
Time of Start: 10:15 
Time at start solutioning: 10:20 => 10.26 (break) => 10:31
Time at start coding:
time at testing: 11:00
time at submission:
"""
'''
m*n
number of rows = m 
number of cols = n
heights[r][c] =>

dp -> m*n => Initialize to None
every cell i can store wether it can take me to both;
and then i can check if that is populated when i traverse, else i can do the real traverse.
iterate over all cells:
    check if dp == None:
        isPacific helper function -> where i can check if a cell can directly reach pacific
        isAtlantic helper function -> same
        for every cell: in all 4 directions - recurse -> ifPacific and ifAtlantic -> true 
'''
class Solution:
    def pacific_atlantic_water_flow(self, heights):
        row = len(heights)
        col = len(heights[0])
        result = []

        for i in range(row):
            for j in range(col):
                if self.canReachPacific(
                    heights, i, j, row, col, [[False for _ in range(col)] for _ in range(row)]) and self.canReachAtlantic(
                        heights, i, j, row, col, [[False for _ in range(col)] for _ in range(row)]):
                    result.append([i,j])
        return result

    def isAtlantic(self, i, j, row, col):
        if i == row-1 or j == col-1:
            return True

    def isPacific(self, i, j):    
        if i == 0 or j == 0:
            return True
    
    def canReachPacific(self, heights, i, j, row, col, visited, height=float('inf')):
        if i < 0 or i >= row or j < 0 or j >= col:
            return False
        
        if visited[i][j]:
            return False
        
        if heights[i][j] > height:
            return False

        if self.isPacific(i, j):
            return True

        visited[i][j] = True
        if self.canReachPacific(
            heights, i+1, j, row, col, visited, heights[i][j]) or self.canReachPacific(
                heights, i-1, j, row, col, visited, heights[i][j]) or self.canReachPacific(
                    heights, i, j+1, row, col, visited, heights[i][j]) or self.canReachPacific(
                        heights, i, j-1, row, col, visited, heights[i][j]):
            return True
        visited[i][j] = False
        return False
    
    def canReachAtlantic(self, heights, i, j, row, col, visited, height=float('inf')):
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