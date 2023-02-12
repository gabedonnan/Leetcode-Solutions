class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #indices = [n for n in range(len(nums))]
        start = 0
        end = len(nums) - 1
        final = 0
        while start <= end:
            pivot = (start + end) // 2
            if target > nums[pivot]:
                start = pivot + 1
                final = pivot + 1
            elif target < nums[pivot]:
                end = pivot - 1
                final = pivot
            else:
                return pivot
        return final
