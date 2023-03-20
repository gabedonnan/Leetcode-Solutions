class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if [flowerbed[max(0,i-1)], flowerbed[i], flowerbed[min(len(flowerbed)-1, i+1)]] == [0,0,0]:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                  return True
        return False
