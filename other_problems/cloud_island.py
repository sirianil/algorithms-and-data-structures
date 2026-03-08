class Solution:
    def __init__(self):
        print("Initiailzied solution")

    def cloud_island(self, island):
        row_count = len(island)
        col_count = len(island[0])
        visited = []
        for _ in range(row_count):
            row = []
            for _ in range(col_count):
                row.append(0)
            visited.append(row)

        total_islands = 0
        for i in range(len(island)):
             for j in range(len(island[0])):
                total_islands = total_islands + self.dfs(island, visited, i, j)

        print("total islands is ", total_islands)

    def dfs(self, island, visited, i, j):
        if i < 0 or j < 0 or i >= len(island) or j >= len(island[0]):
            return 0
        if visited[i][j] or island[i][j] == 0:
            return 0

        visited[i][j] = 1
        if island[i][j] == 1:
            self.dfs(island, visited, i+1,j)
            self.dfs(island, visited, i-1,j)
            self.dfs(island, visited, i,j+1)
            self.dfs(island, visited, i,j-1)
        return 1

if __name__ == '__main__':
    s = Solution()
    s.cloud_island([
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 1, 1],
    ])
