class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indices = []
        for i in range(len(nums)):
            if nums[i] == val:
                indices.append(i)
        for j,index in enumerate(indices):
            nums.pop(index - j)
        return len(nums)
