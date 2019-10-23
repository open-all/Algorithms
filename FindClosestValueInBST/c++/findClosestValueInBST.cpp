#include <cmath>
#include <float.h>
#include <iostream>
using namespace std;

class BST {
public:
  int value;
  BST* left;
  BST* right;

  BST(int val);
  BST& insert(int val);

};

int findClosestValueInBstRecursive(BST* tree, int target);
int findClosestValueInBstHelperRecursive(BST* tree, int target, double closest);

// Average: O(log(n)) time | O(log(n)) space
// Worst: O(n) time | O(n) space
int findClosestValueInBstRecursive(BST* tree, int target) {
  //DBL_MAX is the maximum value that can represented in c++ imported from float
  //for most systems it is 1.79769e+308
  return findClosestValueInBstHelperRecursive(tree, target, DBL_MAX);
}

int findClosestValueInBstHelperRecursive(BST* tree, int target, double closest) {
  //Helper function for binary search
  if (abs(target - closest) > abs(target - tree->value)){
    closest = tree->value;
  }
  if (target < tree->value && tree->left != NULL) {
    return findClosestValueInBstHelperRecursive(tree->left, target, closest);
  } else if (target > tree->value && tree->right != NULL) {
    return findClosestValueInBstHelperRecursive(tree->right, target, closest);
  } else {
    return (int)closest;
  }
}
  int findClosestValueInBstIterative(BST* tree, int target);
  int findClosestValueInBstHelperIterative(BST* tree, int target, double closest);

  // Averge: O(log(n)) time | O(1) space
  // Worest: O(n) time | O(1) space
  int findClosestValueInBstIterative(BST* tree, int target) {
    return findClosestValueInBstHelperIterative(tree, target, DBL_MAX);
  }

  int findClosestValueInBstHelperIterative(BST* tree, int target, double closest) {
    BST* currentNode = tree;
    while (currentNode != NULL) {
      if (abs(target - closest) > abs(target - currentNode->value)) {
        closest = currentNode->value;
      }
      if (target < currentNode->value) {
        currentNode = currentNode->left;
      } else if (target > currentNode->value) {
        currentNode = currentNode->right;
      } else {
        break;
      }
    }
    return (int)closest;
  }
