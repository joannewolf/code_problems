class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        N = len(items)
        items.sort(key=lambda item: item[0])
        max_val = [0] * N # max_val[i]: max(beauty[0:i+1])

        current_max = 0
        for i in range(N):
            if items[i][1] > current_max:
                current_max = items[i][1]
            max_val[i] = current_max

        result = []
        for query in queries:
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right) // 2
                if items[mid][0] <= query:
                    left = mid + 1
                else:
                    right = mid - 1
            # final right is max element index which <= target
            if right == -1:
                result.append(0)
            else:
                result.append(max_val[right])

        return result
