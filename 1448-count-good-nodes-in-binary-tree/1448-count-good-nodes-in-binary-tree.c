/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void dfs(struct TreeNode* root, int *result, int max_val) {
    int current_max;
    
    if (!root) {
        return;
    }
    
    current_max = max_val;
    if (root->val >= max_val) {
        (*result)++;
        current_max = root->val;
    }
    
    dfs(root->left, result, current_max);
    dfs(root->right, result, current_max);
}

int goodNodes(struct TreeNode* root){
    int result = 0;
    
    dfs(root, &result, INT_MIN);
    
    return result;
}