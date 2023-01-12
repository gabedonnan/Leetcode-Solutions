class Solution(object):
    def rob(self, nums):
        return max(nums[0] + self.circle(nums[2:-1]), self.circle(nums[1:]))

    def circle(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            l, r = r, max(l + num, r)  
        return r
