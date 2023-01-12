# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #print(lists)
        final = ListNode(val = 0)
        vals = {}
        flag = True
        while flag:
            flag = False
            for iterator,lis in enumerate(lists):
                if lis != None:
                    flag = True
                    if lis.val not in vals.keys():
                        vals[lis.val] = 1
                        lists[iterator] = lis.next
                    else:
                        vals[lis.val] = vals[lis.val] + 1
                        lists[iterator] = lis.next
        print(vals)
        temp_li = self.unpack_dict(vals)
        print(temp_li)
        for item in temp_li:
            self.add_to_end(item, final)
        return final.next

    def unpack_dict(self, input_dict):
        flag = True
        ordered_keys = sorted(input_dict)
        temp = []
        for item in ordered_keys:
            while input_dict[item] != 0:
                temp.append(ListNode(val=item))
                input_dict[item] -= 1
        return temp


    def add_to_end(self, elem, linked_list):
        temp = linked_list
        while temp.next != None:
            temp = temp.next
        temp.next = elem





