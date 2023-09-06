# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lists = [None for _ in range(k)]
        length = 0
        temp_head = head
        while temp_head is not None:
            length += 1
            temp_head = temp_head.next
        remainder = (length % k) if length > k else 0
        node_size = max(length // k, 1)
        temp_head = head
        index = 0
        ctr = node_size + (1 if remainder != 0 else 0)
        remainder = max(remainder - 1, 0)
        lists[0] = temp_head
        while temp_head is not None:
            
            ctr -= 1
            if ctr == 0:
                ctr = node_size + (1 if remainder != 0 else 0)
                remainder = max(remainder - 1, 0)
                index += 1
                tmp = temp_head.next
                temp_head.next = None
                temp_head = tmp
                try:
                    lists[index] = temp_head
                except IndexError:
                    pass

            else:
                temp_head = temp_head.next

            # print(lists)
        return lists
            
            


