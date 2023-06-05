class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        ln = len(nums)
        while p2 < ln:
            p1 += 1
            curr = nums[p2]
            while nums[p2] == curr:
                p2 += 1
                if p2 == ln:
                    return p1

            nums[p1] = nums[p2]
            
        return p1
