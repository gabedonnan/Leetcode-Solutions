import copy
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        used = [False]*len(nums)
        li = []
        self.dfs(nums, used, li, res)
        return res

    def dfs(self, nums, used, li, res):
        if len(li) == len(nums):
            res.append(copy.deepcopy(li))
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and (nums[i] == nums[i-1]) and not used[i-1]:
                continue
            used[i] = True
            li.append(nums[i])
            self.dfs(nums, used, li, res)
            used[i] = False
            li.pop()
