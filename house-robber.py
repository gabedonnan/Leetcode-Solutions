class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        for num in nums:
            temp = l
            l = max(num + r,l)
            r = temp
        return l  
