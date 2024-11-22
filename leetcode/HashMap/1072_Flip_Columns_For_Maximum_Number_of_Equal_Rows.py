class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        N, M = len(matrix), len(matrix[0])
        TWOS = (1 << M) - 1
        # find the most frequent bit pattern
        bit_dict = {}

        def _add_to_dict(dict, num):
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for row in matrix:
            bits = 0
            for i in range(M):
                bits |= (row.pop() << i)
            # two's complement are consider as same pattern, eg. 101 & 010
            # so bit_dict only keep the key which <= TWOS // 2
            if bits <= TWOS // 2:
                _add_to_dict(bit_dict, bits)
            else:
                _add_to_dict(bit_dict, TWOS - bits)

        return max(bit_dict.values())
