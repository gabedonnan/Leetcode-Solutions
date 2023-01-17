# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        prev = None
        found = False
        while not found:
            if temp == None:
                return head
            if temp.val == n:
                if prev:
                    prev.next = temp.next
                else:
                    head = temp.next
            prev = temp
            temp = temp.next
        return head
  
