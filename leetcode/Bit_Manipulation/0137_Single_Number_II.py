# O(32N), O(1) space
class Solution(object):
    def twos_comp(self, val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)        # compute negative value
        return val                         # return positive value as is

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0b11111111111111111111111111111111
        bits = [0] * 32
        for num in nums:
            num_bit = bin(num & mask)[2:].zfill(32) # return '[0,1]{32}' str
            for i in range(32):
                if num_bit[i] == '1':
                    bits[i] += 1

        for i in range(32):
            bits[i] %= 3

        # convert bit array back to signed int
        bit_str = ''.join(map(str, bits))
        return self.twos_comp(int(bit_str, 2), 32)
