class Solution: #Credit to warrenruud for helping see the logic
    def minFlipsMonoIncr(self, s: str) -> int:
        temp = s.find("1")
        temp_ones = 0
        final = 0
        if s == -1:
            return 0
        
        for num in s[temp:]:
            if num == "1":
                temp_ones += 1
            elif temp_ones > 0:
                temp_ones -= 1
                final += 1
        return final
