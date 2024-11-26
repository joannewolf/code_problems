class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        M, N = len(box), len(box[0])
        grid = [['.'] * M for _ in range(N)]
        for i in range(M):
            stone_count = 0
            for j in range(N):
                if box[i][j] == '#':
                    stone_count += 1
                elif box[i][j] == '*':
                    grid[j][M - i - 1] = '*'
                    for k in range(stone_count):
                        grid[j - 1 - k][M - i - 1] = '#'
                    stone_count = 0

                if j == N - 1:
                    for k in range(stone_count):
                        grid[N - 1 - k][M - i - 1] = '#'
                    stone_count = 0

        return grid
