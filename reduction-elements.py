class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        temp = {}
        final = 0
        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                temp[num] += 1
        counter = 0
        for item in temp:
            final = final + counter * temp[item]
            counter += 1
        return final
