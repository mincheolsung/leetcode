/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    struct TreeNode* cur;
    
    if (p->val > q->val) {
        int *temp = p;
        p = q;
        q = temp;
    }
    
    cur = root;
    
    while (1) {
        if (p->val <= cur->val && cur->val <= q->val) {
            return cur;
        } else if (p->val < cur->val && q->val < cur->val) {
            cur = cur->left;
        } else {
            cur = cur->right;
        }
    }
}