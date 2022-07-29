/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void inorder(struct TreeNode* root, int *result, int *idx) {
    if (root == NULL) {
        return;
    }

    inorder(root->left, result, idx);
    result[*idx] = root->val;
    (*idx)++;
    inorder(root->right, result, idx);
}

int kthSmallest(struct TreeNode* root, int k){
    int i;
    int idx = 0;
    int *result = malloc(10000*sizeof(int));
    if (result == NULL) {
        return -1;
    }

    inorder(root, result, &idx);

    if (idx < k) {
        return -1;
    }
    
    return result[k-1];
}