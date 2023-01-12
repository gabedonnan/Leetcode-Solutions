class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 99999
        flipper = 1
        temp = ""
        final = 0
        for i,char in enumerate(s):
            if i < start and char == "-":
                flipper = -1
                start = i
            elif i < start and char == "+":
                flipper = 1
                start = i
            elif i < start and char in "1234567890":
                temp += char
                start = i
            elif i < start and char != " ":
                return 0
            elif i > start and char not in "1234567890":
                break
            else:
                temp += char
        length = len(temp)
        #print(temp)
        for j in range(length):
            final += 10**(length-j-1) * self.chtoi(temp[j])
            #print(self.chtoi(temp[j]))
        if flipper == 1:
            final = min(final, 2147483647)
        else:
            final = min(final, 2147483648)
        return final * flipper
    
    def chtoi(self, ch):
        numbers = "9876543210"
        realnums = [9,8,7,6,5,4,3,2,1,0]
        return realnums[numbers.find(ch)]
            

