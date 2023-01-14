class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for s in strs:
            if pref == "":
                return pref
            for i in range(min(len(s),len(pref))):
                if s[i] != pref[i]:
                    pref = pref[:i]
                    break
            if len(pref) > len(s):
                pref = pref[:len(s)]
        return pref
