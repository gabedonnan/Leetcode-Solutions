class Solution:
    def reverse(self, x: int) -> int:
        rev = []#
        switch = 1
        if abs(x) != x:
            switch = -1
            x = abs(x)
        final = 0
        while x > 0:
            rev.append(x % 10)#
            x = x // 10
        print(rev)
        for i,num in enumerate(rev[::-1]):
            final += num * (10 ** i)
        final *= switch
        if final > 2147483647:
            return 0
        elif final < -2147483648:
            return 0
        return final
