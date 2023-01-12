class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        removal = []
        x = list(range(len(strs[0])))
        for row_num in range(len(strs)):
            for col_num in x:
                if row_num > 0:
                    if strs[row_num][col_num] < strs[row_num-1][col_num]:
                        removal.append(col_num)
                        count += 1
            x = [elem for elem in x if elem not in removal]
            #removal = []
            #print(removal)
        return count
