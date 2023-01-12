class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        for i,num in enumerate(nums):
            for j, item in enumerate(temp):
                if item + num == target:
                    return [i,j]
            temp.append(num)
