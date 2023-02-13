class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high - low) // 2) + (0 if (high % 2 == 0 and low % 2 == 0) else 1)
