# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        middle = head
        index = 0
        prev = 0.5
        if temp.next == None:
            return temp
        while temp != None:
            temp = temp.next
            if prev % 1 == 0:
                middle = middle.next
            index += 1
            prev += 0.5
        return middle
