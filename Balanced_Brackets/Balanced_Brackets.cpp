#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

// O(n) time | O(n) space
bool balancedBrackets(string str) {
  string openingBrackets = "([{";
  string closingBrackets = ")]}";
  unordered_map<char, char> matchingBrackets {{')', '('}, {']', '['}, {'}', '{'}};
  vector<char> stack;
  for (char character : str) {
    if (openingBrackets.find(character) != string::npos) {
        stack.push_back(character);
      } else if (closingBrackets.find(character) != string::npos) {
        if (stack.size() == 0) {
          return false;
        }
        if (stack[stack.size() - 1] == matchingBrackets[character]) {
          stack.pop_back();
        } else {
          return false;
        }
      }
  }
  return stack.size() == 0;
}

int  main() {
  string brackets[4] = {"()[]{}{","{}()","()([])","{[[[[({(})]]]]}"};
  for (string str : brackets) {
    cout << balancedBrackets(str);
    cout << endl;
  }
  return 0;
}
