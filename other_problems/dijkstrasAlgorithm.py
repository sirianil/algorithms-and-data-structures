import heapq

class DijkstrasAlgo:
    def __init__(self):
        return
    
    def build_adj_list(self, edges_and_weights):
        self.adj_list = {}
        for i in range(len(edges_and_weights)):
            connection = edges_and_weights[i]
            node1 = connection[0]
            node2 = connection[1]
            weight = connection[2]
            if node1 not in self.adj_list:
                self.adj_list[node1] = [(node2, weight)]
            else:
                self.adj_list[node1].append((node2, weight))

            if node2 not in self.adj_list:
                self.adj_list[node2] = [(node1, weight)]
            else:
                self.adj_list[node2].append((node1, weight))

    def shortest_path_from_source(self, source):
        # Dictionary of node to distance; will be returned
        distances = {}
        for key in self.adj_list.keys():
            distances[key] = float('inf')

        pq = [] # (Node and weight)
        visited = set() # hashset of visited nodes

        heapq.heappush(pq, (0, source))
        distances[source] = 0

        while len(pq) != 0:
            print("-----Start of while loop-----")
            current_weight, current_node = heapq.heappop(pq)
            print("Current node is ", current_node, " Current weight is ", current_weight)

            for neighbor in self.adj_list[current_node]:
                v, w = neighbor[0], neighbor[1]
                print("Processing neighbor ", v, " with weight ", w)
                if w + current_weight < distances[v]:
                    distances[v] = w + current_weight
                    print("New weight of ", v, " is ", distances[v])
                
                if v not in visited:
                    heapq.heappush(pq, (distances[v], v))
            visited.add(current_node)
            print("visited is ", visited)
            print("-----End of while loop-----")
        return distances
    
    def dfs(self, source):
        visited = set()

        stack = [source]
        while len(stack) != 0:
            node = stack.pop()

            if node in visited:
                continue
            else:
                visited.add(node)
                print("Visiting node ", node)

            for neighbor, _ in self.adj_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


if __name__ == '__main__':
    d = DijkstrasAlgo()

    edges_and_weights = [
        ["S", "A", 5],
        ["S", "D", 1],
        ["A", "D", 2],
        ["A", "B", 4],
        ["B", "C", 6],
        ["D", "C", 8],
        ["D", "E", 5],
        ["E", "C", 10],
    ]
    d.build_adj_list(edges_and_weights)
    # print("Distances is ", d.shortest_path_from_source("S"))
    d.dfs("S")
