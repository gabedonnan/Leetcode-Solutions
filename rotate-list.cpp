/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getListLength(ListNode* curr) {
        int fin = 0;
        while (curr != NULL) {
            fin++;
            curr = curr->next;
        }
        return fin;
    }

    ListNode* rotateRight(ListNode* head, int k) {
        int len = getListLength(head);
        if (len == 0) {
            return head;
        }
        k = k % len;
        if (k == 0) {
            return head;
        }

        ListNode* secondHalfTail = head;
        for (int i = 0; i < (len - 1) - k; i++) {
            secondHalfTail = secondHalfTail->next;
        }
        

        ListNode* firstHalfHead = secondHalfTail->next;
        ListNode* finalVal = firstHalfHead;
        secondHalfTail->next = NULL;
        while (firstHalfHead->next != NULL) {
            firstHalfHead = firstHalfHead->next;
        }
        firstHalfHead->next = head;
        return finalVal;
    }
};
