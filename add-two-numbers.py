# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lFinal = ListNode()
        temp = lFinal
        while l1 != None or l2 != None:
            if l1 != None:
                self.chainAdd(temp, l1.val)
                l1 = l1.next
            if l2 != None:
                self.chainAdd(temp, l2.val)
                l2 = l2.next
            if temp.next == None and (l1 != None or l2 != None):
                temp.next = ListNode()
            temp = temp.next
        return lFinal


    def chainAdd(self, lis, num):
        if lis.val + num > 9:
            if lis.next != None:
                lis.val = lis.val + num - 10
                self.chainAdd(lis.next, 1)
            else:
                lis.val = lis.val + num - 10
                lis.next = ListNode(val = 1)
        else:
            lis.val = lis.val + num
