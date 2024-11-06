class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        val_bits = [] # list of tuple (val, bits)
        for num in arr:
            val = num
            bits = 0
            while num != 0:
                bits += num % 2
                num //= 2
            val_bits.append((val, bits))

        def my_comp(a, b):
            if a[1] != b[1]:
                return (a[1] - b[1])
            else:
                return (a[0] - b[0])

        val_bits.sort(cmp=my_comp)

        return [val for val, bits in val_bits]