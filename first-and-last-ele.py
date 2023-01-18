class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), abs(len(nums) - 1 - nums[::-1].index(target))]
        except:
            return [-1,-1]
