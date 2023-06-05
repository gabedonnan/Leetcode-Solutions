class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p_main = m + n - 1  # Pointer to array location of next addition
        # Pointers start from the back to avoid shifting the array along
        while p2 >= 0:  # Iterate until p2 is negative, this means both p1 and p2 are exhausted
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_main] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_main] = nums2[p2]
                p2 -= 1
            p_main -= 1
