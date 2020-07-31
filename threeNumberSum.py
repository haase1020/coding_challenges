# write a function that takes in a non-empty array of distinct ints representing a target
# sum. The fn should find all triplets in the array that sum up to the taget sum and return
# a two-dimensional array of these triplets. The numbers in each triplet should be ordered in ascending
# order, and the triplets themselves should be ordered in ascending order with respect to the
# numbers they hold.


# ****hint*** sort array and then use L and R pointer!!
# time complexity: 0(n^2)  space complexity: 0(n)
# sort array 0(n(log(n))
# need currentNumber cn, left, right, and currentSum cs
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets


print(threeNumberSum([122, 3, 1, 2, -6, 5, -8, 6], 0))
# expect [[-8,2,6],[-8,3,5],[-6,1,5]]
