class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)
        remain = [gas[i] - cost[i] for i in range(N)]
        # remain[i]: the remaining gas moving from station i to i+1
        # target is to find whether there is a starting point suth that all prefix sum >= 0

        left, right = 0, N - 1
        gas_sum = 0
        while left < right:
            if gas_sum + remain[left] >= 0: # can move to next station
                gas_sum += remain[left]
                left += 1
            else: # try start from previous station
                gas_sum += remain[right]
                right -= 1
        # final left is the circuit end point
        if gas_sum + remain[left] >= 0:
            return (left + 1) % N
        else:
            return -1
