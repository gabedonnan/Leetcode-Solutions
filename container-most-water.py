class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rpointer = len(height) - 1
        maximum = 0
        lpointer = 0
        lhighest = 0
        rhighest = 0
        area = 0
        while rpointer > lpointer:
            if height[lpointer] > lhighest or height[rpointer] > rhighest:
                area = min(height[lpointer], height[rpointer]) * abs(lpointer-rpointer)
            if area > maximum:
                maximum = area
            if height[lpointer] > lhighest:
                lhighest = height[lpointer]
            if height[rpointer] > rhighest:
                rhighest = height[rpointer]
            if height[lpointer] > height[rpointer]:
                rpointer -= 1
            elif height[lpointer] < height[rpointer]:
                lpointer += 1
            else:
                lpointer += 1
                rpointer -= 1
        return maximum


