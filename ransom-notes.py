class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        final = defaultdict(int)

        if len(ransomNote) > len(magazine):
            return False
        for letter in ransomNote:
            final[letter] -= 1
        for letter in magazine:
            final[letter] += 1
        for letter in final:
            if final[letter] < 0:
                return False
        return True
