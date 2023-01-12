class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        count = 0
        for c in costs:
            if c <= coins:
                coins -= c
                count += 1
            else:
                return count
        return count
