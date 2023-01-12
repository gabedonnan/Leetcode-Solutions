class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       
        temp = str(x) #String solution
        for i in range(len(temp) // 2):
            if temp[i] != temp[-(i+1)]:
                return False
        return True
