class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dependencies = {i: [] for i in range(n)}
        for [u, v] in edges:
            dependencies[v].append(u)

        champions = [node for node, parents in dependencies.items() if not parents]
        if len(champions) != 1:
            return -1
        else:
            return champions[0]
