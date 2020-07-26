# with double for loop will take 0(n^2)
# with hashtable O(n) for time and space complexity
# can also use two pointers (if array is sorted) starting at both ends:time is 0(n log n), and space 0(1)

# # double for loop option: 0(n^2) time | 0(1) space
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []


# # hashtable option: 0(n) time | 0(n) space
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [potentialMatch, num]
#         else:
#             nums[num] = True
#     return []


# two pointer option: 0(n log n) time | 0(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
