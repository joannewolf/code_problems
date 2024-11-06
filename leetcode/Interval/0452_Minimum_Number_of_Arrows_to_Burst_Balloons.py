class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        # sort by x_end
        points.sort(key=lambda point: point[1])
        result = 1
        # greedily take the first x_end
        arrow = points[0][1]
        for i in range(1, N):
            if arrow < points[i][0]:
                result += 1
                arrow = points[i][1]

        return result
