"""
Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any
two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most
one pair of numbers summing up to the target sum.
Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]
"""

import random
import time

# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) -1):
        firstNumber = array[i]
        for j in range(i + 1, len(array)):
            secondNumber = array[j]
            if firstNumber + secondNumber == targetSum:
                return [firstNumber, secondNumber]
    return[]

#O(n) time | O(n) space
def twoNumberSumBest(array, targetSum):
    #this solution uses a dictonary/hashmap
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []



if __name__ == '__main__':
    sampleList = []
    for x in range(100000000):
        sampleList.append(random.randint(1,1000))

    targetSum = 666
    t0 = time.time()
    print(twoNumberSum(sampleList,targetSum))
    t1 = time.time()
    print(t1 - t0)
    t0 = time.time()
    print(twoNumberSumBest(sampleList,targetSum))
    t1 = time.time()
    print(t1 - t0)
