/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *cur;
    struct ListNode *prev;
    struct ListNode *next;
    struct ListNode prehead;

    if (!head) {
        return NULL;
    }
    
    prehead.next = head;
    cur = &prehead;
    prev = cur;
    next = cur->next;

    while (next) {
        cur = next;
        next = cur->next;
        cur->next = prev;
        prev = cur;
    }
    
    head->next = NULL;
    
    return cur;
}