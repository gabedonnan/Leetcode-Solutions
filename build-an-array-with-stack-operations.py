class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        cur = 1
        for item in target:
            while cur < item:
                output.append("Push")
                output.append("Pop")
                cur += 1
            
            output.append("Push")
            cur += 1
        return output
