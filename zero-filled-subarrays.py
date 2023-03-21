class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        flag = False
        total = 0
        for i in range(len(nums)):
            if not flag and nums[i] == 0:
                flag = True
                startLoc = i
            if flag and nums[i] != 0:
                flag = False
                total += self.addTotal(i - startLoc)
        if flag:
            total += self.addTotal(len(nums) - startLoc)
        return total

    @staticmethod
    def addTotal(length: int) -> int:
        length += 1
        return int((length * (length-1)) / 2)
