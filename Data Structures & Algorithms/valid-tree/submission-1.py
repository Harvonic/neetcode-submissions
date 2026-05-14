class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = {}
        neighbors = {}

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited[node] = True

            for i in neighbors[node]:
                if i != parent and not dfs(i, node):
                    return False
            
            return True

        for i in range(n):
            neighbors[i] = []

        for i in edges:
            neighbors[i[0]].append(i[1])
            neighbors[i[1]].append(i[0])

        return dfs(0, None) and len(visited) == n
    



        