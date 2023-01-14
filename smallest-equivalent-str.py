class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        relations = {}
        
        for i in range(len(s1)):
            if s1[i] not in relations:
                relations[s1[i]] = []
            if s2[i] not in relations:
                relations[s2[i]] = []


            relations[s1[i]].append(s2[i])
            relations[s2[i]].append(s1[i])

            temp_middle = []

            temp_middle.extend(relations[s2[i]])
            temp_middle.extend(relations[s1[i]])

            relations[s1[i]] = temp_middle
            relations[s2[i]] = temp_middle

            relations[s1[i]] = list(set(relations[s1[i]]))
            relations[s2[i]] = list(set(relations[s2[i]]))
        
        changedflag = False
        while not changedflag:
            changedflag = True
            for item in relations:
                for char in relations[item]:
                    if len(relations[char]) > len(relations[item]):
                        changedflag = False
                        relations[item] = list(set(relations[char] + relations[item]))
                        break
        
        final = ""

        for char in baseStr:
            if char in relations:
                final += min(relations[char])
            else:
                final += char

        return final
