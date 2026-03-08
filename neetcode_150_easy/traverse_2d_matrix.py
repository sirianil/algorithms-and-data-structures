def traverse_2d_matrix(grid):
    if len(grid) == 0:
        return None

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            print(grid[i][j])
    
if __name__ == '__main__':
    grid = [[]]
    traverse_2d_matrix(grid)