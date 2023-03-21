class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        def partition(low: int, high: int) -> int:
            nonlocal nums
            pivot = nums[high]
            i = low
            for j in range(low, high, 1):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        def quicksort(low: int, high: int) -> None: 
            nonlocal nums
            if low < high:
                qVal = partition(low, high)
                quicksort(low, qVal - 1)
                quicksort(qVal + 1, high)

        quicksort(0, len(nums) - 1)
