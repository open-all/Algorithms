"""
Three number sum

    Write a function that takes in a non-empty array of distinct
    integers and an integer representing a target sum.
    The function should find all triplets in the arry that sum up to the target
    sum and return a two-dimensional array of all these triplets.
    The number in each triplet should be ordered in ascending order,
    and the triplets themselves should be ordered in ascending order
    with respect to the numbers they hold. If no three numbers sum up 
    to the target sum, the function should return an empty array
    
    Sample input: [12,3,1,2,-6,5,-8,6], 0
    Sample output: [[-8,2,6],[-8,3,5],[-6,1,5]]
"""

# O(n^2) runtime | O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    """
    This algorithm uses a binary search on a sorted list to find all possilbe         combinations of 3 numbers within the list that add to equal the target sum.
    If there are no sums that equal the target, it will return an empty list.
    """
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets