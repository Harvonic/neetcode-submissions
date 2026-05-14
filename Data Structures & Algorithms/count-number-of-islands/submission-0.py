class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0

        numRow = len(grid) - 1
        numCol = len(grid[0]) - 1

        def bfs(grid, x, y, depth):
            nonlocal count
            # out of bounds
            if x > numRow or y > numCol or x < 0 or y < 0:
                return
            
            # not an island or already visited
            if grid[x][y] == "0" or grid[x][y] == "-1":
                return
            
            # the first time we see a new island, so we count it
            if depth == 0:
                count += 1
        
            grid[x][y] = "-1" # mark visited


            bfs(grid, x+1, y, depth + 1)
            bfs(grid, x-1, y, depth + 1)
            bfs(grid, x, y + 1, depth + 1)
            bfs(grid, x, y - 1, depth + 1)

        for i in range(numRow + 1):
            for j in range(numCol + 1):
                bfs(grid, i, j, 0)
        
        print(grid)

        return count
            



        