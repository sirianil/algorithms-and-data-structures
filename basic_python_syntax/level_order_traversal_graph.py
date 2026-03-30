from collections import deque

class Graph:
    '''
    1-> 2
    |
    |-> 3
    |-> 4
    '''
    def __init__(self):
        self.adj = {
            1: [2, 4],
            2: [3, 4],
            3: [1],
            4: [2, 3]
        }

    def bfs(self):
        queue = deque()
        queue.append(root)

        cur_level = 1
        visited = { root }
        while queue:
            cur_len = len(queue)

            for _ in range(cur_len):
                node = queue.popleft()

                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            cur_level += 1

    def iterative_dfs(self):
        visited = {1}
        stack = [ 1 ]

        while stack:
            node = stack.pop()

            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)


if __name__ == '__main__':
    g = Graph()
    g.iterative_dfs()
