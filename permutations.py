class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = self.search([], nums)
        numlen = len(nums)
        permutations = [permutations[i * numlen:(i + 1) * numlen] for i in range((len(permutations) + numlen - 1) // numlen )] #oneliner splitting list into chunks
        return permutations

    def search(self, current: List[int], possible: List[int]) -> List[int]:
        final = []
        if possible == []:
            return []
        elif len(possible) == 1:
            return current + [possible[0]]
        for num in possible:
            final.extend(self.search(current + [num], [p for p in possible if p != num]))
        return final
