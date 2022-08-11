/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void traversal(struct TreeNode* root, int* idx, int *result) {
    if (root == NULL) {
        return;
    }
    
    traversal(root->left, idx, result);
    result[(*idx)++] = root->val;
    traversal(root->right,idx, result);
}


bool isValidBST(struct TreeNode* root){
    if (root == NULL) {
        return true;
    }
    int idx = 0;
    int result[10000] = {0};
 
    traversal(root, &idx, result);
    
    int i;
    for (i = 0; i < idx-1; i++) {
        if (result[i] >= result[i+1]) {
            return false;
        }
    }

    return true;
}
    
    