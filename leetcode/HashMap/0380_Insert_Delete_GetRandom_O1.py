class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.num_index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.num_index:
            return False
        else:
            self.nums.append(val)
            self.num_index[val] = len(self.nums) - 1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.num_index:
            return False
        else:
            index = self.num_index.pop(val)
            last_num = self.nums.pop()
            if index != len(self.nums):
                self.nums[index] = last_num
                self.num_index[last_num] = index
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        import random
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()