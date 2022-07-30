class Solution {
public:
  vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {

    unordered_map<string, int> m;
    vector<TreeNode*> res;
    serialize(root, m, res);
    return res;
  }
private:
  string serialize(TreeNode* root, unordered_map<string, int>&
  m, vector<TreeNode*>& res){
    if (!root) return "#";
    string key = to_string(root->val) + ","
                  + serialize(root->left, m, res) + ","
                  + serialize(root->right, m, res);

                  if (++m[key] == 2)
                    res.push_back(root);
                  return key;
  }
};
