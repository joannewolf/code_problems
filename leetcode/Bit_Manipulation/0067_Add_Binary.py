class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        # convert str to int list, least significant bit on the left
        a_bits = [int(i) for i in a[::-1]]
        b_bits = [int(i) for i in b[::-1]]
        overflow = 0
        result = []

        for i in range(max(len_a, len_b)):
            if i >= len_a:
                bit_sum = b_bits[i] + overflow
            elif i >= len_b:
                bit_sum = a_bits[i] + overflow
            else:
                bit_sum = a_bits[i] + b_bits[i] + overflow

            result.append(bit_sum % 2)
            overflow = bit_sum // 2

        if overflow:
            result.append(overflow)

        result = [str(bit) for bit in result]
        result = ''.join(result)[::-1]
        return result
