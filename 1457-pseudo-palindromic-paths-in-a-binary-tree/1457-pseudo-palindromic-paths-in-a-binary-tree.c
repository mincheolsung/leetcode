/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void dfs(struct TreeNode* root, int path, int *answer) {
    path ^= (1 << root->val);
    
    if (root->left == NULL && root->right == NULL) {
        if ((path & (path - 1)) == 0) {
            (*answer)++;
        }
    }
        
    if (root->left) {
        dfs(root->left, path, answer);
    }

    if (root->right) {
        dfs(root->right, path, answer);
    }
}

int pseudoPalindromicPaths (struct TreeNode* root){
    int answer = 0;
    dfs(root, 0, &answer);
    return answer;
}