import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, 1
        for i in range(n):
            temp = l + r
            l = r
            r = temp
        return l
