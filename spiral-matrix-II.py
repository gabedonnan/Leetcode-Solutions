class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        length = n
        arr = [[0] * n for _ in range(n)]
        i, j = 0, 0
        di, dj = 1, 0
        k = 1
        steps = n-k
        countdown = 2
        curr = 1
        sq = n ** 2
        while curr < sq:
            arr[j][i] = curr
            curr += 1
            i += di
            j += dj
            steps -= 1

            if countdown == 0:
                k += 1
                countdown = 2

            if steps == 0:
                di, dj = self.turnRight(di, dj)
                steps = n - k
                countdown -= 1
            
            

        if n % 2 != 0 :
            arr[i][j] = curr
        else:
           arr[i+1][j-1] = curr 
        
        return arr

            
    
    def turnRight(self, di, dj):
        if di == 0:
            if dj == 1:
                return -1, 0
            else:
                return 1, 0
        else:
            if di == 1:
                return 0, 1
            else:
                return 0, -1
