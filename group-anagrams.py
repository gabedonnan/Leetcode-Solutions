class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for s in strs:
            sort_str = "".join(sorted(s))
            if sort_str not in temp:
                temp[sort_str] = [s]
            else:
                temp[sort_str].append(s)
        final = []
        for t in temp:
            final.append(temp[t])
        return final
