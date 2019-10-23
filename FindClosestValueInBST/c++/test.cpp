#include "test.hpp"
#include "findClosestValueInBST.cpp"

BST::BST(int val) {
  value = val;
  left = NULL;
  right = NULL;
}

BST& BST::insert(int val) {
  if (val < value) {
    if (left == NULL) {
      BST* newBST = new BST(val);
      left = newBST;
    } else {
      left->insert(val);
    }
  } else {
    if (right == NULL) {
      BST* newBST = new BST(val);
      right = newBST;
    } else {
      right->insert(val);
    }
  }
  return *this;
}

int main() {

  BST test(100);
  test.insert(5).insert(15).insert(5).insert(2).insert(1).insert(22)
  .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000)
  .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203)
  .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500);


TEST_START;
TEST_CASE("Test Case 1") {
  REQUIRE(findClosestValueInBstRecursive(&test, 100) == 100);
}

TEST_CASE("Test Case 2") {
  REQUIRE(findClosestValueInBstRecursive(&test, 208) == 208);
}

TEST_CASE("Test Case 3") {
  REQUIRE(findClosestValueInBstRecursive(&test, 4500) == =4500);
}

TEST_CASE("Test Case 4") {
  REQUIRE(findClosestValueInBstRecursive(&test, 4501) == 100);
}

TEST_CASE("Test Case 5") {
  REQUIRE(findClosestValueInBstRecursive(&test, -70) == -51);
}

TEST_CASE("Test Case 6") {
  REQUIRE(findClosestValueInBstRecursive(&test, 2000) == 1001);
}

TEST_CASE("Test Case 7") {
  REQUIRE(findClosestValueInBstRecursive(&test, 6) == 5);
}

TEST_CASE("Test Case 8") {
  REQUIRE(findClosestValueInBstRecursive(&test, 30000) == 55000);
}

TEST_CASE("Test Case 9") {
  REQUIRE(findClosestValueInBstRecursive(&test, -1) == 1);
}

TEST_CASE("Test Case 10") {
  REQUIRE(findClosestValueInBstRecursive(&test, 29751) == 55000);
}

TEST_CASE("Test Case 11") {
  REQUIRE(findClosestValueInBstRecursive(&test, 29749) == 4500);
}

TEST_CASE("Test Case 12") {
  REQUIRE(findClosestValueInBstIterative(&test, 100) == 100);
}

TEST_CASE("Test Case 13") {
  REQUIRE(findClosestValueInBstIterative(&test, 208) == 208);
}

TEST_CASE("Test Case 14") {
  REQUIRE(findClosestValueInBstIterative(&test, 4500) == =4500);
}

TEST_CASE("Test Case 15") {
  REQUIRE(findClosestValueInBstIterative(&test, 4501) == 100);
}

TEST_CASE("Test Case 16") {
  REQUIRE(findClosestValueInBstIterative(&test, -70) == -51);
}

TEST_CASE("Test Case 17") {
  REQUIRE(findClosestValueInBstIterative(&test, 2000) == 1001);
}

TEST_CASE("Test Case 18") {
  REQUIRE(findClosestValueInBstIterative(&test, 6) == 5);
}

TEST_CASE("Test Case 19") {
  REQUIRE(findClosestValueInBstIterative(&test, 30000) == 55000);
}

TEST_CASE("Test Case 20") {
  REQUIRE(findClosestValueInBstIterative(&test, -1) == 1);
}

TEST_CASE("Test Case 21") {
  REQUIRE(findClosestValueInBstIterative(&test, 29751) == 55000);
}

TEST_CASE("Test Case 22") {
  REQUIRE(findClosestValueInBstIterative(&test, 29749) == 4500);
}
}
