/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* invertTree(struct TreeNode* root){
    struct TreeNode* temp;
    
    if (root == NULL) {
        return NULL;
    }

    root->left = invertTree(root->left);
    root->right = invertTree(root->right);
    
    temp = root->right;
    root->right = root->left;
    root->left = temp;
    
    return root;
}