class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = ""
        current_len = 0
        longest = 0
        start = 0
        flag = False
        ind = 0
        while ind < len(s):
            if s[ind] in seen:
                seen = ""
                if current_len > longest:
                    longest = current_len
                current_len = 0
                start += 1
                ind = start
                flag = True

            
            if not flag:
                current_len += 1
                seen += s[ind]
                ind += 1
            flag = False
        return max(longest, current_len)


