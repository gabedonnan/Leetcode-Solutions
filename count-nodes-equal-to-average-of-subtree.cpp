/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int counter = 0;
public:
    std::pair<int, int> subtreeSum(TreeNode* root) {
        int current_sum = root->val;
        int current_size = 1;
        if (root->left != NULL) {
            auto [subtree_size_l, subtree_sum_l] = subtreeSum(root->left);
            current_sum += subtree_sum_l;
            current_size += subtree_size_l;
        }
        if (root->right != NULL) {
           auto [subtree_size_r, subtree_sum_r] = subtreeSum(root->right);
            current_sum += subtree_sum_r;
            current_size += subtree_size_r;
        }
        
        if (current_sum / current_size == root->val) {
            counter += 1;
        }

        return std::make_pair(current_size, current_sum);
    }
    int averageOfSubtree(TreeNode* root) {
        subtreeSum(root);
        return counter;
    }
};
