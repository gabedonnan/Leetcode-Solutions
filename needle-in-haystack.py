class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        rpointer = 0
        if len(needle) > len(haystack):
            return -1
        for lpointer in range(len(haystack)):
            rpointer = lpointer
            while haystack[rpointer] == needle[rpointer-lpointer]:
                rpointer += 1
                if rpointer-lpointer > len(needle) - 1:
                    return lpointer
                if rpointer > len(haystack) - 1:
                    return -1
        return -1
