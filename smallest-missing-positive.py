class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = 1
        num_dict = {}
        for num in nums:
            num_dict[num] = 1
        while smallest < 2147483648:
            if smallest not in num_dict:
                return smallest
            smallest += 1
        #return 
        
