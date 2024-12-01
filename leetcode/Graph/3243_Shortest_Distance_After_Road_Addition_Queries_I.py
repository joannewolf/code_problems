class Solution(object):
    def BFS(self, n, graph):
        checked = set()
        current_nodes = set([0])
        step = 0
        while current_nodes:
            next_nodes = set()
            if n - 1 in current_nodes:
                return step

            for node in current_nodes:
                if node in checked:
                    pass
                else:
                    next_nodes.update(set(graph[node]) - checked)
                checked.add(node)

            step += 1
            current_nodes = next_nodes

        return step

    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        graph = {i: [] for i in range(n)} # graph[i]: the reachable next nodes from node i
        for i in range(n - 1):
            graph[i].append(i + 1)

        for [u, v] in queries:
            graph[u].append(v)
            result.append(self.BFS(n, graph))

        return result
