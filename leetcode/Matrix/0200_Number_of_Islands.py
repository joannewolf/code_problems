class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    count += 1
                    # Use BFS to fill island
                    stack = [(i, j)]
                    while stack:
                        (x, y) = stack.pop()
                        if grid[x][y] == '1':
                            grid[x][y] = 'a' # mark with other char
                            if x > 0:
                                stack.append((x - 1, y))
                            if x < M - 1:
                                stack.append((x + 1, y))
                            if y > 0:
                                stack.append((x, y - 1))
                            if y < N - 1:
                                stack.append((x, y + 1))

        return count
