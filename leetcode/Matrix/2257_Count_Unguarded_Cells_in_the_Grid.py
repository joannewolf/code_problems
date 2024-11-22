# O(mn)
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[''] * n for _ in range(m)]
        for [i, j] in guards:
            grid[i][j] = 'g'
        for [i, j] in walls:
            grid[i][j] = 'w'

        # horizontal check
        for i in range(m):
            # from left to right
            can_see = (grid[i][0] == 'g')
            for j in range(1, n):
                if grid[i][j] == 'g':
                    can_see = True
                elif grid[i][j] == 'w':
                    can_see = False
                elif can_see:
                    grid[i][j] = 'x'
            # from right to left
            can_see = (grid[i][n - 1] == 'g')
            for j in range(n - 2, -1, -1):
                if grid[i][j] == 'g':
                    can_see = True
                elif grid[i][j] == 'w':
                    can_see = False
                elif can_see:
                    grid[i][j] = 'x'

        # vertical check
        for j in range(n):
            # from up to botton
            can_see = (grid[0][j] == 'g')
            for i in range(1, m):
                if grid[i][j] == 'g':
                    can_see = True
                elif grid[i][j] == 'w':
                    can_see = False
                elif can_see:
                    grid[i][j] = 'x'
            # from botton to up
            can_see = (grid[m - 1][j] == 'g')
            for i in range(m - 2, -1, -1):
                if grid[i][j] == 'g':
                    can_see = True
                elif grid[i][j] == 'w':
                    can_see = False
                elif can_see:
                    grid[i][j] = 'x'

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '':
                    count += 1
        return count

# O(mn + g*(m + n)), TLE
class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[''] * n for _ in range(m)]
        for [i, j] in guards:
            grid[i][j] = 'g'
        for [i, j] in walls:
            grid[i][j] = 'w'

        for [I, J] in guards:
            # guard up side
            for i in range(I - 1, -1, -1):
                if grid[i][J] == '':
                    grid[i][J] = 'x'
                elif grid[i][J] == 'w':
                    break
            # guard down side
            for i in range(I + 1, m):
                if grid[i][J] == '':
                    grid[i][J] = 'x'
                elif grid[i][J] == 'w':
                    break
            # guard left side
            for j in range(J - 1, -1, -1):
                if grid[I][j] == '':
                    grid[I][j] = 'x'
                elif grid[I][j] == 'w':
                    break
            # guard right side
            for j in range(J + 1, n):
                if grid[I][j] == '':
                    grid[I][j] = 'x'
                elif grid[I][j] == 'w':
                    break

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '':
                    count += 1
        return count
