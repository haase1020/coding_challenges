# write a function that takes in a sorted array of integers as well as a target integer.
# the function should use the binary search algorithm to determine if the target integer
# is contained in the array and should return it's index if it is, otherwise -1.
# if a list is sorted, odds are you want to use a binary search!

# time complexity: 0(log(n)) where n is the length of array
# space = 0(1) or if recursive 0(log(n))
# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) - 1)


# def binarySearchHelper(array, target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     potentialMatch = array[middle]
#     if target == potentialMatch:
#         return middle
#     elif target < potentialMatch:
#         return binarySearchHelper(array, target, left, middle - 1)
#     else:
#         return binarySearchHelper(array, target, middle + 1, right)

# iterative is 0(log(n)) time  and 0(1) space


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
