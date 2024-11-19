class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(code)
        prefix_sum = [0] * N # prefix_sum[i] = sum(code[:i+1])
        prefix_sum[0] = code[0]
        for i in range(1, N):
            prefix_sum[i] = prefix_sum[i - 1] + code[i]

        if k == 0:
            return [0] * N

        print(prefix_sum)
        result = [None] * N
        if k > 0:
            for i in range(N - k):
                result[i] = prefix_sum[i + k] - prefix_sum[i]
            for i in range(N - k, N):
                result[i] = (prefix_sum[N - 1] - prefix_sum[i]) + prefix_sum[k - (N - i)]
        else:
            k = abs(k)
            print(N - 1, k + 2)
            for i in range(N - 1, k, -1):
                result[i] = prefix_sum[i - 1] - prefix_sum[i - k - 1]
            result[k] = prefix_sum[k - 1]
            for i in range(k - 1, 0, -1):
                result[i] = prefix_sum[i - 1] + (prefix_sum[N - 1] - prefix_sum[N - 1 - (k - i)])
            result[0] = (prefix_sum[N - 1] - prefix_sum[N - 1 - k])

        return result
