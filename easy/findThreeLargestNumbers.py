# Prompt: Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array
# of the three largest integers in the input array.
# the function should return duplicate integers if necessary. For examples it should return [10,10,12] for an input
# array of [10,5,9,10,12]. This will return the array as a sorted array in increasing order.

# time complexity is 0(n) where n is length of input array, space is 0(1)
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
