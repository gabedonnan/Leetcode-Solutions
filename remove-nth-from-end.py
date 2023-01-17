# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevList = [head]
        found = False
        while not found:
            if prevList[-1].next != None:
                prevList.append(prevList[-1].next)
            else:
                found = True
        if n != 1 and n != len(prevList):
            prevList[-(n+1)].next = prevList[-(n-1)]
        elif n != len(prevList):
            prevList[-(n+1)].next = None
        else:
            head = head.next
        return head
