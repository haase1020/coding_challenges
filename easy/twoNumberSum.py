# with double for loop will take 0(n^2)
# with hashtable O(n) for time and space complexity
# can also use two pointers (if array is sorted) starting at both ends:time is 0(n log n), and space 0(1)


# two pointer option: 0(nlog(n)) time | 0(1) space
def twoNumberSum(array, targetSum):
    newArray = []
    array.sort()
    print(array)
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            newArray.append([array[left], array[right]])
            right -= 1
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return newArray


array = [3, 5, 2, -4, 8, 11]
print(twoNumberSum(array, 7))
