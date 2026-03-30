from collections import deque

def find_closest_dasher(board, start):
    if not board or not board[0]:
        return -1 
    
    rows = len(board)
    cols = len(board[0])

    queue = deque()
    queue.append(start)

    dashmarts = []
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = set()
    visited.add(start)

    while queue:
        cur_len = len(queue)
        count = 0
        while count < cur_len:
            i, j = queue.popleft()

            if board[i][j] == 'D':
                dashmarts.append((i,j))
            
            for d in directions:
                next_cell = i+d[0], j+d[1]
                if next_cell[0] >= 0 and next_cell[1] >= 0 and next_cell[0] < rows and next_cell[1] < cols and next_cell not in visited:
                    visited.add(next_cell)
                    queue.append(next_cell) 
            count += 1
        if len(dashmarts) > 0:
            return dashmarts                       
        distance += 1

    return -1