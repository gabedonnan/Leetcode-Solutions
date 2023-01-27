class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for j,char in enumerate(s):
            if char in chars:
                chars[char][0] = -1
            else:
                chars[char] = [1,j]
        
        for ch in chars:
            if chars[ch][0] == 1:
                return chars[ch][1]
        return -1
