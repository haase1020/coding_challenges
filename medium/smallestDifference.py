# write a function that takes in two non-empty arrays of ints, finds the pair or numbers (one
# from each array) whose absolute difference is closest to zero, and returns an array
# containing these two numbers, with the number from the first array in the first position.


# time complexity: 0(n log(N) + M log(M)) where length of N is for array1 and M for array2
# space complexity: 0(1) --> sorting arrays in place

def smallestDifference(arrayOne, arrayTwo):
    # sort arrays in ascending order first
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
